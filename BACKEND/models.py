from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

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

class RideRequest(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)

    from_: str = Field(default='Base Station')
    destination: str
    request_time: datetime
    assigned_puller_id: int | None = Field(default=None)
    status: str = Field(default='pending')    # pending, accepted, rejected, completed
