import logging
from pyclbr import Function
from typing import Any, List, Optional

from app.database_init import get_db
from app.repos.task_repo import FilterQuery, TasksRepo
from app.schemas.task import ToDoTaskCreate, ToDoTaskOut, ToDoTaskUpdate
from app.usecases.errors import ToDoRepoError
from fastapi import Depends
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)


class ToDoInteractor:
    """Interactor responsible for manipulation of interactions with Tasks"""

    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.task_repo: TasksRepo = TasksRepo(db)

    def add(self, task: ToDoTaskCreate) -> str:
        """
        Add task
        """
        try:
            task_id = self.task_repo.create(task=task)
            return task_id
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def update(self, task: ToDoTaskUpdate) -> None:
        """
        Update task
        """
        try:
            self.task_repo.update(task=task)
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def get(self, id: str) -> Optional[ToDoTaskOut]:
        """
        Retrieve tasks
        """
        try:
            task = self.task_repo.get(id=id)
            if task is None:
                return None

            return ToDoTaskOut(**task.__dict__)
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def all(self) -> List[ToDoTaskOut]:
        """
        Retrieve all tasks
        """
        try:
            tasks = self.task_repo.get()
            return [ToDoTaskOut(**task.__dict__) for task in tasks if task is not None]
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def retreive(self, filters: FilterQuery) -> List[ToDoTaskOut]:
        """
        Filter tasks
        """
        try:
            tasks = self.task_repo.filter(filters=filters)
            return [ToDoTaskOut(**task.__dict__) for task in tasks if task is not None]
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def remove(self, id: str) -> None:
        """
        Clear tasks
        """
        try:
            self.task_repo.delete(id=id)
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)

    def clear(self) -> int:
        """
        Clear tasks
        """
        return self.task_repo.clear()

    def _run(self, func: Function, **kwargs) -> Any:
        try:
            return func(**kwargs)
        except Exception as e:
            logger.exception(e)
            raise ToDoRepoError(e)


todo_interactor = ToDoInteractor()
