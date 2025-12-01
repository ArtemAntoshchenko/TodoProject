from sqlalchemy import create_engine, Column, Integer, String, DATETIME
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from enum import Enum
from dotenv import load_dotenv
from datetime import datetime
import os

Base=DeclarativeBase()

class TodoStatusEnum(str, Enum):
    PENDING='pending'
    IN_PROGRESS='in_progress'
    COMPLETED='completed'

todo=status_enum=Enum(TodoStatusEnum, name='todostatus', create_type=True)

class TodoDB(Base):
    __tablename__='todos'

    id=Column(Integer, primary_key=True, index=True)
    title=Column(String(200), nullable=False)
    description=Column(String(1000),  nullable=False)
    status=Column(Enum(TodoStatusEnum),default=TodoStatusEnum.PENDING)
    create_at=Column(DATETIME, default=datetime.timezone.utc, onupdate=datetime.timezone.utc, nullable=False)
    update_at=Column(DATETIME, default=datetime.timezone.utc, onupdate=datetime.timezone.utc, nullable=False)
    __table_args__=(
        {'postgresql_using':'btree'},
    )
POSTGRES_USER=os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD','password')
POSTGRES_HOST=os.getenv('POSTGRES_HOST','host')
POSTGRES_PORT=os.getenv('POSTGRES_PORT','5432')
POSTGRES_DB=os.getenv('POSTGRES_DB','todo_db')

SQLALCHEMY_DATABASE_URL=(f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
                        f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}')

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=20,
    max_overdlow=30,
    pool_pre_ping=True
)
Base.metadata.create_all(bind=engine)

SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def get_db():
    db=SessionLocal
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()