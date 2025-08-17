from datetime import datetime, timedelta

import boto3
from app.constants import Constants
from app.managers import UniqueIDGenerationManager
from app.models import URLMapping
from settings.settings import settings

dynamodb = boto3.resource(
    'dynamodb',
    region_name=settings.aws_region,
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    endpoint_url=settings.dynamodb_endpoint_url
)
table = dynamodb.Table('UrlMappings')

class CreateShortURLManager:
    @classmethod
    def get_short_url(cls, request_body):
        response = table.query(
            IndexName='LongUrlIndex',
            KeyConditionExpression='long_url = :long_url',
            ExpressionAttributeValues={
                ':long_url': request_body.long_url
            }
        )
        
        for item in response.get('Items', []):
            if datetime.fromisoformat(item['expires_at']) > datetime.now():
                return URLMapping(**item)

        uid_generation = UniqueIDGenerationManager(Constants.UNIQUE_ID_LENGTH)
        
        while True:
            short_url = uid_generation.generate_unique_id()
            response = table.get_item(Key={'short_url': short_url})
            if 'Item' not in response:
                break

        new_url = URLMapping(
            long_url=request_body.long_url,
            short_url=short_url,
            expires_at=cls.get_expiration_date(request_body),
            created_at=datetime.now(),
            custom_alias=request_body.custom_alias,
            user_id=request_body.user_id,
        )
        item_to_put = new_url.dict()
        item_to_put['expires_at'] = new_url.expires_at.isoformat()
        item_to_put['created_at'] = new_url.created_at.isoformat()
        
        table.put_item(Item=item_to_put)
        
        return new_url

    @classmethod
    def get_expiration_date(cls, request_body):
        if not request_body.expiration_date or request_body.expiration_date is None:
            return datetime.now() + timedelta(days=30)
        return request_body.expiration_date
