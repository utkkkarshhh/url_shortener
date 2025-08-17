from fastapi import HTTPException
from starlette import status
from app.constants import Constants

from settings.dynamodb_config import DynamoDB


class FetchLongURLManager:
    
    @classmethod
    def get_long_url(cls, unique_id):
        dynamodb = DynamoDB()
        table = dynamodb.get_table('UrlMappings')
        short_url = Constants.SHORT_URL.format(unique_id=unique_id)
        try:
            response = table.get_item(Key={'short_url': short_url})
        except Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
        
        if 'Item' not in response:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Short URL not found")
        
        return response['Item']['long_url']
