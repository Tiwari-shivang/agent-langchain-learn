from pydantic import BaseModel, ConfigDict

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