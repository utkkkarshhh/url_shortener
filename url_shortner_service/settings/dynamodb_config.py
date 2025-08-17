import boto3
from botocore.exceptions import ClientError
from fastapi import HTTPException
from starlette import status

from app.utils.logger import logger
from settings.settings import get_settings

settings = get_settings()


class DynamoDB:
    def __init__(self):
        self.dynamodb = boto3.resource(
            "dynamodb",
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=settings.dynamodb_endpoint_url,
        )
        logger.info("Successfully connected to DynamoDB")

    def get_table(self, table_name: str):
        try:
            return self.dynamodb.Table(table_name)
        except ClientError as e:
            logger.error(e.response["Error"]["Message"])
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Could not connect to DynamoDB",
            )


import boto3
from app.utils.logger import logger
from settings.settings import settings
from app.models.create_table import create_url_mappings_table


def setup_dynamodb():
    try:
        client = boto3.client(
            "dynamodb",
            region_name=settings.aws_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=settings.dynamodb_endpoint_url,
        )
        logger.info("Successfully connected to DynamoDB")
        create_url_mappings_table()
        return client
    except Exception as e:
        logger.error(f"Could not connect to DynamoDB: {e}")
        return None

