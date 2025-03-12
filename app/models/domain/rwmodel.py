import datetime
from pydantic import BaseModel

def convert_datetime_to_realworld(dt: datetime.datetime) -> str:
    # 例: ISOフォーマットに変換
    return dt.isoformat()

def convert_field_to_camel_case(field: str) -> str:
    parts = field.split('_')
    return parts[0] + "".join(word.capitalize() for word in parts[1:])

class RWModel(BaseModel):
    model_config = {
        "populate_by_name": True,
        "json_encoders": {datetime.datetime: convert_datetime_to_realworld},
        "alias_generator": convert_field_to_camel_case,
    }

