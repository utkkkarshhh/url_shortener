import json
from datetime import datetime
from enum import Enum

from fastapi import Response
from pydantic import BaseModel


def json_datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


class ResponseHandler(Response):
    def __init__(
        self,
        content_obj=None,
        data=None,
        success=None,
        status=None,
        message=None,
        errors=None,
        headers=None,
        content_type="application/json",
    ):
        content = {}

        if content_obj:
            content = self._make_json_serializable(content_obj)
        if data:
            content["data"] = self._make_json_serializable(data)
        if success is not None:
            content["success"] = success
        if message:
            content["message"] = self._make_json_serializable(message)
        if errors:
            content["errors"] = self._make_json_serializable(errors)

        content = json.dumps(content, default=json_datetime_serializer)

        super().__init__(
            content=content, status_code=status, headers=headers, media_type=content_type
        )

    def _make_json_serializable(self, obj):
        if isinstance(obj, BaseModel):
            return obj.dict()
        elif isinstance(obj, Enum):
            return obj.value
        elif isinstance(obj, dict):
            return {k: self._make_json_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_json_serializable(item) for item in obj]
        return obj
