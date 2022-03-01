from datetime import datetime
from typing import List, Optional

from app.constants import TaskStatus
from pydantic import BaseModel


class Base(BaseModel):
    id: str
    text: Optional[str] = None
    status: Optional[str] = TaskStatus.active.value
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class ToDoTaskCreate(Base):
    id: str
    text: str
    status: str

    class Config:
        orm_mode = True
        schema_extra = {
            "text": "test",
            "status": "ACTIVE",
            "created_at": "2021-08-12T00:00:00Z",
            "updated_at": "2021-08-12T00:00:00Z",
        }


class ToDoTaskUpdate(Base):
    id: str
    text: str
    status: str

    class Config:
        orm_mode = True
        schema_extra = {
            "id": "53b26667-aef5-4f19-91bd-7da50574186e",
            "text": "test",
            "status": "ACTIVE",
            "created_at": "2021-08-12T00:00:00Z",
            "updated_at": "2021-08-12T00:00:00Z",
        }


class ToDoTaskOut(Base):
    class Config:
        orm_mode = True
        schema_extra = {
            "id": "some-id",
            "text": "test",
            "status": "ACTIVE",
            "created_at": "2021-08-12T00:00:00Z",
            "updated_at": "2021-08-12T00:00:00Z",
        }


class FilterQueryInput(BaseModel):
    ids: Optional[List[str]] = None
    status: Optional[List[str]] = None

    class Config:
        orm_mode = True
        schema_extra = {
            "ids": ["some-id", "some-other-id"],
            "status": ["ACTIVE", "COMPLETED"],
        }
