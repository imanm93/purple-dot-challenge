import uuid
from datetime import datetime
from unittest import TestCase, mock

from app.apis.v1 import api as v1
from app.apis.v1.api import FilterQueryInput
from app.constants import TaskStatus
from app.schemas.task import ToDoTaskCreate, ToDoTaskUpdate
from app.usecases.todo_interactor import ToDoInteractor
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.testclient import TestClient

from todo_api.app.schemas.task import ToDoTaskOut

test_app = FastAPI(title="test_client")
test_app.include_router(
    v1.router,
    prefix="/v1",
    tags=["v1"],
)


class TestApi(TestCase):
    def test_add(self, client: TestClient = TestClient(test_app)) -> None:
        mock_id = str(uuid.uuid4())
        mock_task = ToDoTaskCreate(
            id=mock_id,
            text="test",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        mock.patch.object(
            ToDoInteractor,
            "add",
            return_value="b85f8640-3bc2-4ac7-b40f-ed74ae055e3f",
        )

        response = client.post("/v1/create", json=jsonable_encoder(mock_task))

        assert response.status_code == status.HTTP_201_CREATED

    def test_get_by_id(self, client: TestClient = TestClient(test_app)) -> None:
        mock_id = "b85f8640-3bc2-4ac7-b40f-ed74ae055e3f"
        mock_out = ToDoTaskOut(
            id="b85f8640-3bc2-4ac7-b40f-ed74ae055e3f",
            text="test_one",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        mock.patch.object(
            ToDoInteractor,
            "get",
            return_value=mock_out,
        )

        response = client.get(f"/v1/filter/{mock_id}")

        assert response.status_code == status.HTTP_200_OK
        assert response.json()["text"] == "test_one"

    def test_get_all(self, client: TestClient = TestClient(test_app)) -> None:
        response = client.get("/v1/")

        assert response.status_code == status.HTTP_200_OK

        tasks = response.json()
        assert len(tasks) > 0

    def test_filter(self, client: TestClient = TestClient(test_app)) -> None:
        query = FilterQueryInput(
            ids=["b85f8640-3bc2-4ac7-b40f-ed74ae055e3f"],
            status=[TaskStatus.active.value],
        )
        response = client.get("/v1/filter", json=jsonable_encoder(query))

        assert response.status_code == status.HTTP_200_OK

        tasks = response.json()
        assert len(tasks) == 1

    def test_update(self, client: TestClient = TestClient(test_app)) -> None:
        mock_id = "b85f8640-3bc2-4ac7-b40f-ed74ae055e3f"
        task = ToDoTaskUpdate(
            id=mock_id,
            text="test_one",
            status="ACTIVE",
            created_at=datetime(2021, 8, 12, 0, 0, 0),
            updated_at=datetime(2021, 8, 12, 0, 0, 0),
        )
        response = client.put(f"/v1/{mock_id}", json=jsonable_encoder(task))

        assert response.status_code == status.HTTP_200_OK

        updated_task = response.json()
        assert updated_task["success"] == "updated task"
