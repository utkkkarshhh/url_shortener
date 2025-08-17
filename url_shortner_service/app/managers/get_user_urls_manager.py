from fastapi import HTTPException
from starlette import status
from boto3.dynamodb.conditions import Key, Attr

from settings.dynamodb_config import DynamoDB


class GetUserURLsManager:

    @classmethod
    def get_user_urls(cls, user_id):
        dynamodb = DynamoDB()
        table = dynamodb.get_table('UrlMappings')
        try:
            response = table.scan(
                FilterExpression=Attr('user_id').eq(user_id)
            )
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

        return response.get('Items', [])
