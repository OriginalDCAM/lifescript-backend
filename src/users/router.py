from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.users import crud, schemas

from src.database import get_db

users = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@users.get('/login')
async def login():
    return 'login'


@users.get('/register')
async def register():
    return 'register'


@users.post('/login')
async def login():
    return 'test'


@users.post('/register')
async def register():
    return 'test'


@users.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
