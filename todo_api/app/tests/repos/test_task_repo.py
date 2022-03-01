from unittest import TestCase

import pytest
from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from app.repos.task_repo import TasksRepo
from app.tests.test import TestBase

from todo_api.app.repos.errors import ToDoTaskUpdateError
from todo_api.app.schemas.task import ToDoTaskUpdate


class TestTaskRepo(TestBase):
    def setUp(self) -> None:
        super().setUp()
        session = UnifiedAlchemyMagicMock()
        self.task_repo = TasksRepo(db=session)

    def test_create(self) -> None:
        self.task_repo.create(task=self.mock_task_one)

        resp = self.task_repo.get(id=self.mock_task_one.id)

        assert resp.id == self.mock_task_one.id
        assert resp.text == self.mock_task_one.text
        assert resp.status == self.mock_task_one.status

    def test_read(self) -> None:
        self.task_repo.create(task=self.mock_task_one)

        resp = self.task_repo.get(id=self.mock_task_one.id)

        assert resp.id == self.mock_task_one.id
        assert resp.text == self.mock_task_one.text
        assert resp.status == self.mock_task_one.status

    def test_read_all(self) -> None:
        for mock_task in self.mock_tasks:
            self.task_repo.create(mock_task)

        resp = self.task_repo.get()

        assert len(resp) == 4

    def test_update(self) -> None:
        id = self.task_repo.create(task=self.mock_task_two)
        update_task = ToDoTaskUpdate(
            id=id,
            text="some update",
            status=self.mock_task_two.status,
            created_at=self.mock_task_two.created_at,
            updated_at=self.mock_task_two.updated_at,
        )

        _ = self.task_repo.update(task=update_task)

        task = self.task_repo.get(id=id)
        assert task.id == update_task.id

    def test_update_error(self) -> None:
        update_task = ToDoTaskUpdate(
            id="random",
            text="update",
            status=self.mock_task_two.status,
            created_at=self.mock_task_two.created_at,
            updated_at=self.mock_task_two.updated_at,
        )

        with TestCase.assertRaises(self, ToDoTaskUpdateError):
            self.task_repo.update(task=update_task)

    def test_delete(self) -> None:
        test_id = self.mock_task_one.id
        self.task_repo.delete(id=test_id)

        task = self.task_repo.get(id=test_id)

        assert task is None

    def test_clear(self) -> None:
        self.task_repo.clear()

        tasks = self.task_repo.get()

        assert len(tasks) == 0
