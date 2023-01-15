from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Page(Base):
    __tablename__ = "pages"

    id = Column(Integer, primary_key=True, index=True)
    page_number = Column(Integer)
    page_content = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship("Book", back_populates="pages")
