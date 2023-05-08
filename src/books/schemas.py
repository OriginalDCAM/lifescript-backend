from pydantic import BaseModel, Field

from src.pages.schemas import Page


class BookBase(BaseModel):
    title: str
    description: str | None = Field(...)


class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: int
    is_public: bool
    pages: list[Page] = []

    class Config:
        orm_mode = True
