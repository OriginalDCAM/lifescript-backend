from pydantic import BaseModel


class PageBase(BaseModel):
    page_content: str
    page_number: int


class PageCreate(PageBase):
    pass


class Page(PageBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True
