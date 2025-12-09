import os
from typing import List, Optional
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, validator, field_validator
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..','..','.env'))
class Settings(BaseSettings):
    PROJECT_NAME:str='Task Manager'
    VERSION:str='1.0.0'
    API_V1_STR:str='/api/v1'
    DEBUG:bool=False

    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_HOST:str='localhost'
    POSTGRES_PORT:str='5432'
    POSTGRES_DB:str

    DATABASE_URL:Optional[PostgresDsn]=None
    @field_validator('DATABASE_URL', mode='before')
    @classmethod
    def assemble_db_connection(cls, v:Optional[str], values):
        if isinstance(v, str):
            return v
        return PostgresDsn.build()