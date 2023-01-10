from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


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
