import uuid
from datetime import datetime

import pytz
from app.database_init import Base
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import configure_mappers


class ToDoTask(Base):
    """Task model contains details"""

    __tablename__ = "todo_task"

    id = Column(UUID(), primary_key=True, index=True, default=uuid.uuid4())
    text = Column(String(150), nullable=False)
    status = Column(
        String(100),
        default="ACTIVE",
        nullable=False,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(tz=pytz.utc),
        nullable=False,
    )
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(tz=pytz.utc),
        nullable=False,
    )


configure_mappers()
