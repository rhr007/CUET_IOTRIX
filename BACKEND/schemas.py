from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    phone: str
    password: str
