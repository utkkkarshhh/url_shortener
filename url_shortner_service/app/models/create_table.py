import boto3
from app.utils.logger import logger
from botocore.exceptions import ClientError
from settings.settings import settings


def create_url_mappings_table():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name=settings.aws_region,
        aws_access_key_id=settings.aws_access_key_id,
        aws_secret_access_key=settings.aws_secret_access_key,
        endpoint_url=settings.dynamodb_endpoint_url
    )
    table_name = 'UrlMappings'
    try:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'short_url',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'short_url',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'long_url',
                    'AttributeType': 'S'
                }
            ],
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'LongUrlIndex',
                    'KeySchema': [
                        {
                            'AttributeName': 'long_url',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 5,
                        'WriteCapacityUnits': 5
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        logger.info(f"Table '{table_name}' created successfully.")
        return table
    except ClientError as e:
        if e.response['Error']['Code'] == 'ResourceInUseException':
            logger.info(f"Table '{table_name}' already exists.")
            return dynamodb.Table(table_name)
        else:
            logger.error(f"Error creating table: {e}")
            raise
