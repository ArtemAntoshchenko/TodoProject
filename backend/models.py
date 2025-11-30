from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime
from enum import Enum

class TodoStatus(str, Enum):
    PENDING='pending'
    IN_PROGRESS='in_progress'
    COMPLETED='completed'

class TodoBase(BaseModel):
    title:str = Field(..., min_length=1, max_length=200, description='Название задачи')
    description:Optional[str]=Field(None, max_length=1000,  description='Описание задачи')
    status:TodoStatus=Field(default=TodoStatus.PENDING,  description='Статус задачи')

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title:Optional[str]=Field(None, min_length=1, max_length=200)
    description:Optional[str]=Field(None, max_length=1000)
    status:Optional[TodoStatus]=Field(None)

class TodoInDB(TodoBase):
    id:int
    created_at:datetime
    updatet_at:datetime

    model_config = ConfigDict(from_attributes=True)

class TodoResponse(TodoInDB):
    pass

