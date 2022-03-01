## 🤓 Backend Design

### 🏗️ Code Design

We used clean architecture, DDD, and REST API design in mind when developing this todo app. In following these principles, we are able to achieve software best practices of SOLID.

```
todo_api
    ↳ tables
    ↳ repo
    ↳ schemas
    ↳ interactors
    ↳ api
```

The above structure allows you to easily add new outer layers without the need to touch underlying business logic.

### 📞 API Design

You can view the spec at `/redoc`, it will appear as below:

![redoc](/docs/redoc.png)

### 🧱 Constants

```python
class ToDoState(Enum):
    active = "active"
    completed = "completed"
```

### 📚 DB Model Design

```python
class ToDoTaskModel(BaseModel):
    id: UUID
    text: str
    state: str
    created_at: datetime
    updated_at: datetime
```

**constraints:** one task cannot be added to multiple lists atm

#### How to run api?

1. run `docker-compose up`
2. open your browser to `http://localhost:8000`

