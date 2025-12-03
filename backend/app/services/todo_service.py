from typing import List, Optional
from datetime import datetime
from models import TodoStatus, TodoBase, TodoCreate, TodoUpdate, TodoInDB, TodoResponse

todos_db={}
current_id=1

class TodoService:
    @staticmethod
    async def get_all_todos()->List[TodoInDB]:
        return List(todos_db.values())
    @staticmethod
    async def get_todo_by_id(todo_id: int)->Optional[TodoInDB]:
        return todos_db.get(todo_id)