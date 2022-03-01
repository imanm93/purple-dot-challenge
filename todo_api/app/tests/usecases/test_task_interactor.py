from alchemy_mock.mocking import UnifiedAlchemyMagicMock
from app.tests.test import TestBase
from app.usecases.todo_interactor import ToDoInteractor


class TestTaskInteractor(TestBase):
    def setUp(self) -> None:
        session = UnifiedAlchemyMagicMock()
        self.task_interactor = ToDoInteractor(db=session)
        return super().setUp()

    def test_add(self):
        pass

    def test_remove(self):
        pass
