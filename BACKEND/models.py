from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone: str = Field(unique=True)
    password: str 
    is_admin: bool = Field(default=False)
    is_active: bool = Field(default=False)
    current_lat: float | None = Field(default=None)
    current_lng: float | None = Field(default=None)
    points: int = 0