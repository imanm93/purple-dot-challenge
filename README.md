# 🟣

[![Python 3.8+](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![license](https://img.shields.io/badge/license-Apache-blue.svg)](https://img.shields.io/badge/license-Apache-blue)

source code for the 🟣 take home challenge

## App Setup

### Requirements

- docker
- docker-compose
- make

Please see installations instructions [here](some-link).

Now, run `make start` - that's all, enjoy the app! 😎

## 🤓 Backend Design

### 🏗️ Code Design

We used clean architecture, DDD, and REST API design in mind when developing this todo app. In following these principles, we are able to achieve software best practices of SOLID (and nowadays TOUCH).

```
todo_api
    ↳ tables
    ↳ repo
    ↳ schemas
    ↳ interactors
    ↳ api
```

The above structure allows you to easily add new outer layers without the need to touch underlying business logic. For example, ...

### 📞 API Design

| URI | METHOD | DESCRIPTION |
| --- | --- | --- |
| `/v1/todo` | `GET` | Retrieves todos |
| `/v1/todo/?state=<state>` | `DELETE` | Deletes todos in state |
| `/v1/todo` | `POST` | Creates a new todo |
| `/v1/todo/?state=<state>,<state>` | `GET` | Retrieves filtered todos |
| `/v1/todo/{id}` | `GET` | Retrieves a (single) todo |
| `/v1/todo/{id}` | `PUT` | Updates a todo |
| `/v1/todo/{id}` | `DELETE` | Deletes todo |

You can view the spec at `/redoc`, it will appear as below:

![redoc](/docs/redoc.png)

### Payload Design

`GET` request response

```js
{
	"id": "...",
	"text": "...",
	"operations": [
        {
            "method": "PUT",
            "href": "/...",
            "Expects": {}
        },
        {
            "method": "POST",
            "href": "/...",
            "Expects": {}
        },
        {
            "method": "DELETE",
            "href": "/...",
        }
    ]
}
```

`POST` request payload

```js
{
	"id": "...",
	"text": "...",
    "state": "...",
}
```

`POST` request response

```js
{
	"id": "...",
	"text": "...",
	"operations": [
        {
            "method": "PUT",
            "href": "/...",
            "Expects": {}
        },
        {
            "method": "GET",
            "href": "/...",
            "Expects": {}
        },
        {
            "method": "DELETE",
            "href": "/...",
        }
    ]
}
```

### 🧱 Constants

```python
class ToDoState(Enum):
    active = "active"
    completed = "completed"
```

### 📚 DB Model Design

```python
class ToDoListModel(BaseModel):
    id: str
    name: str
    created_at: datetime
    updated_at: datetime
```

```python
class ToDoTaskModel(BaseModel):
    id: str
    text: str
    state: str
    list_id: str (FK)
    created_at: datetime
    updated_at: datetime
```

**relationship:** `ToDoListModel` 1 → n `ToDoTaskModel` (one to many)

**constraints:** one task cannot be added to multiple lists atm

### Tests

...

## 🧑‍🎨 Frontend Design

We have used the concept of smart and dumb components to design our client.

- **Dumb components** are responsible for only visual representation of our data and passing back any interactions from the user. It does not care where or what is done to the data it displays.

We have also used storybook to allow non-tech teammates (designer or product ) to easily view and interact with the different states of the foundational UI components. Buttons, Filters, List, Items and so on.

- **Smart components** represent components that manipulate state / interact with data.

We want these components to represent concepts such as Tasks and Lists.

Other than the above smart and dump components we have a generic api client (using axios) which we use to interact with our backend through an intermediate `todoAPI` interface.

#### How to run storybook?

1. run `docker-compose up`
2. open your browser to `http://localhost:3001`

#### How to run client?

1. run `docker-compose up`
2. open your browser to `http://localhost:3000`

#### How to run api?

1. run `docker-compose up`
2. open your browser to `http://localhost:80`

### Tests

...

## Next Steps

Some ideas around where we can take this app next. 

*this is by no means an exhaustive list of ideas (there never can be!)*

- **Pagination:** As the application scales it will become unrealistic to retrieve lists with more than hundreds of thousands or millions of tasks. Thus, pagination is one of the mechanisms through which we can minimize this load. It can be done by index or time at which a task is created.

- **Tasks w/ images, descriptions:** Atm tasks consists of only text. This is not great from an UX perspective where users may want to add links or images.

- **Multiple Lists:** A user may want to group certain tasks into one list and others into another list. Therefore, we can support for multiple lists. We can do this by adding a new set of endpoints which are the equivalent CRUD ops for tasks at the list level.
