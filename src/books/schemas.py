from pydantic import BaseModel

from src.pages.schemas import Page


class BookBase(BaseModel):
    title: str
    description: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author_id: int
    pages: list[Page] = []

    class Config:
        orm_mode = True
