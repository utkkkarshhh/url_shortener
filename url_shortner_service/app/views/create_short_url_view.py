from app.constants import ResponseMessages
from app.managers import CreateShortURLManager
from app.schemas import CreateShortURLRequestSchema, CreateShortURLResponseSchema
from app.utils import ResponseHandler
from fastapi import status


class CreateShortURLView:
    def post(request_body: CreateShortURLRequestSchema):
        url_mapping = CreateShortURLManager.get_short_url(request_body)
        
        response_data = CreateShortURLResponseSchema(
            short_url=url_mapping.short_url,
            long_url=url_mapping.long_url,
            created_at=url_mapping.created_at,
            expiration_date=url_mapping.expires_at
        )

        return ResponseHandler(
            message=ResponseMessages.SHORT_URL_CREATED_SUCCESSFULLY,
            success=True,
            status=status.HTTP_200_OK,
            data=response_data
        )
