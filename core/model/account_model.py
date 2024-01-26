from dataclasses_avroschema.pydantic import AvroBaseModel
from pydantic import Field

class AccountID(AvroBaseModel):
    id: str = Field(description='Id to id an account.')
