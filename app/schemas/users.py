from pydantic import BaseModel, ConfigDict
from uuid import UUID

class UserCreateReq(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    date_of_birth: str
    gender: str
    country: str
    city: str

class SuccessResponse(BaseModel):
    message: str
    model_config=ConfigDict(from_attributes=True)

class UserDetails(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str
    date_of_birth: str
    gender: str
    country: str
    city: str
    model_config=ConfigDict(from_attributes=True)