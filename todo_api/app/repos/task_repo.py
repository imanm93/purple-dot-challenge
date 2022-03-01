import logging
from dataclasses import dataclass
from sqlite3 import DatabaseError
from typing import List, Optional, Union

from app.repos.errors import (ToDoTaskCreateError, ToDoTaskDeleteError,
                              ToDoTaskReadError, ToDoTaskUpdateError)
from app.schemas.task import ToDoTaskCreate, ToDoTaskUpdate
from app.tables.todo_task import ToDoTask
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


@dataclass
class FilterQuery:
    ids: Optional[List[str]]
    status: Optional[List[str]]


class TasksRepo:
    """CRUD ops for task model"""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get(self, id: str = None) -> Union[List[ToDoTask], ToDoTask, None]:
        try:
            if id is None:
                tasks = self.db.query(ToDoTask).all()
                return tasks

            task = self.db.query(ToDoTask).filter_by(id=id).first()
            return task
        except DatabaseError as e:
            logger.exception(e)
            raise DatabaseError(e)
        except Exception as e:
            logger.exception(e)
            raise ToDoTaskReadError(e)

    def filter(self, filters: FilterQuery) -> List[ToDoTask]:
        query = self.db.query(ToDoTask)
        if filters.ids is not None:
            query = query.filter(ToDoTask.id.in_(filters.ids))

        if filters.status is not None:
            query = query.filter(ToDoTask.status.in_(filters.status))

        return query.all()

    def create(self, task: ToDoTaskCreate) -> str:
        try:
            new_task = ToDoTask(**task.dict())
            self.db.add(new_task)
            self.db.commit()
            return new_task.id
        except DatabaseError as e:
            logger.exception(e)
            raise DatabaseError(e)
        except Exception as e:
            logger.exception(e)
            raise ToDoTaskCreateError(e)

    def update(self, task: ToDoTaskUpdate) -> None:
        exists = self.db.query(ToDoTask).filter_by(id=task.id).first()
        if exists is None:
            raise ToDoTaskUpdateError(f"[{task.id}]: item does not exist")

        self.db.delete(exists)
        self.db.commit()

        self.db.add(
            ToDoTask(
                id=task.id,
                text=task.text,
                status=task.status,
                created_at=task.created_at,
            )
        )
        self.db.commit()

    def delete(self, id: str) -> None:
        try:
            record = self.db.query(ToDoTask).filter_by(id=id).first()
            if record is None:
                return None

            self.db.delete(record)
            self.db.commit()
        except DatabaseError as e:
            logger.exception(e)
            raise DatabaseError(e)
        except Exception as e:
            logger.exception(e)
            raise ToDoTaskDeleteError(e)

    def clear(self) -> int:
        try:
            num_deleted = self.db.query(ToDoTask).delete()
            self.db.commit()
            return num_deleted
        except DatabaseError as e:
            logger.exception(e)
            raise DatabaseError(e)
        except Exception as e:
            logger.exception(e)
            raise ToDoTaskDeleteError(e)
