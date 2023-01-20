from pydantic import BaseModel, EmailStr, ValidationError, validator, Field, constr
from src.books.schemas import Book


class UserBase(BaseModel):
    first_name: str = Field(min_length=1, max_length=32)
    username: constr(regex="[A-Za-z0-9-_]+$",
                     to_lower=True, strip_whitespace=True)
    email: EmailStr


class UserCreate(UserBase):
    password: str = Field(min_length=8, max_length=32)


class UserUpdate(UserBase):
    pass


class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=32)


class User(UserBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
