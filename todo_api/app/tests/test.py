from datetime import datetime
from unittest import TestCase

from todo_api.app.schemas.task import ToDoTaskCreate


class TestBase(TestCase):
    def setUp(self) -> None:
        self.mock_task_one = ToDoTaskCreate(
            id="6cb41857-3b33-4310-ad54-f1563edc5b9f",
            text="test1",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        self.mock_task_two = ToDoTaskCreate(
            id="9c236b70-3346-4e3b-b472-3c7036e4b574",
            text="test2",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        self.mock_task_three = ToDoTaskCreate(
            id="18d0e961-ed1a-46b9-89b7-ba6bca642763",
            text="test3",
            status="COMPLETED",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        self.mock_task_four = ToDoTaskCreate(
            id="79debebc-2783-4b0e-bc40-cf63878f10d5",
            text="test4",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )

        self.mock_tasks = [
            self.mock_task_one,
            self.mock_task_two,
            self.mock_task_three,
            self.mock_task_four,
        ]
