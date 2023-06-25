from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from entities.solid.todo import TodoTask

app = FastAPI()


@app.post("/todos/create")
async def create_todo(todo: TodoTask):
    return todo


@app.get("/todos/{id_}")
async def get_todo(id_: str):
    todo_list = ['todo1', 'todo2', 'todo3']
    return {todo_list[int(id_)]}


@app.delete("/todos/{id_}")
async def delete_todo_by_id(id_: str):
    todo_list = ['todo1', 'todo2', 'todo3']
    popped = todo_list.pop(int(id_))
    return {
        "remaining": todo_list,
        'deleted': popped
    }


@app.put("/todos/{id_}")
async def update_todo_by_id(id_: str, todo: TodoTask):
    todo_list = ['todo1', 'todo2', 'todo3']
    todo_list[int(id_)] = todo
    return {
        "all_content": todo_list,
        'changed': todo
    }


def swagger_documentation():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Todo App",
        version="2.5.0",
        description="This is the schema of the Todo App.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = swagger_documentation
