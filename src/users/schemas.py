from pydantic import BaseModel
from src.books.schemas import Book


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
