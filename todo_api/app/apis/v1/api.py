import logging
from typing import Any, Dict, List, Optional

from app.apis.v1.errors import ToDoInteractorError
from app.database_init import get_db
from app.repos.task_repo import FilterQuery
from app.schemas.task import (FilterQueryInput, ToDoTaskCreate, ToDoTaskOut,
                              ToDoTaskUpdate)
from app.usecases.todo_interactor import ToDoInteractor
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

Resp = Dict[str, str]
router = APIRouter()


@router.post(
    "/create", response_model=ToDoTaskCreate, status_code=status.HTTP_201_CREATED
)
def add_task(data: ToDoTaskCreate, db: Session = Depends(get_db)) -> Any:
    """Add new tasks"""
    try:
        task = ToDoTaskCreate(**data.dict())
        todo_interactor = ToDoInteractor(db=db)
        todo_interactor.add(task=task)
        return task
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.get(
    "/filter/{id}", response_model=Optional[ToDoTaskOut], status_code=status.HTTP_200_OK
)
def read_tasks(id: str = None, db: Session = Depends(get_db)) -> Any:
    """Get specific task"""
    try:
        if id is None:
            return None

        todo_interactor = ToDoInteractor(db=db)
        task = todo_interactor.get(id=id)
        return task
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.get("/", response_model=List[ToDoTaskOut], status_code=status.HTTP_200_OK)
def read_all_tasks(db: Session = Depends(get_db)) -> Any:
    """Get all tasks"""
    try:
        todo_interactor = ToDoInteractor(db=db)
        tasks = todo_interactor.all()
        return tasks
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.get("/filter", response_model=List[ToDoTaskOut], status_code=status.HTTP_200_OK)
def read_filtered_tasks(body: FilterQueryInput, db: Session = Depends(get_db)) -> Any:
    """Get filtered tasks"""
    try:
        todo_interactor = ToDoInteractor(db=db)

        def _build_filters_query(filters: FilterQueryInput) -> FilterQuery:
            return FilterQuery(**filters.__dict__)

        filters = _build_filters_query(body)
        tasks = todo_interactor.retreive(filters=filters)
        return tasks
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.put("/{id}", response_model=Resp, status_code=status.HTTP_200_OK)
def update_task(id: str, body: ToDoTaskUpdate, db: Session = Depends(get_db)) -> Any:
    """Edit a task"""
    try:
        task = ToDoTaskUpdate(**body.dict())
        todo_interactor = ToDoInteractor(db=db)
        todo_interactor.update(task=task)
        return {"success": "updated task"}
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.delete("/{id}", response_model=Resp, status_code=status.HTTP_200_OK)
def delete_task(id: str, db: Session = Depends(get_db)) -> Any:
    """Delete a task"""
    try:
        todo_interactor = ToDoInteractor(db=db)
        todo_interactor.remove(id=id)
        return {"success": f"removed task: {id}"}
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)


@router.delete("/clear", response_model=Resp, status_code=status.HTTP_200_OK)
def clear_tasks(db: Session = Depends(get_db)) -> Any:
    """Delete all tasks"""
    try:
        todo_interactor = ToDoInteractor(db=db)
        num_deleted = todo_interactor.clear()
        return {"success": f"removed {num_deleted} tasks"}
    except HTTPException as e:
        logger.exception(e)
        raise HTTPException(e)
    except Exception as e:
        logger.exception(e)
        raise ToDoInteractorError(e)
