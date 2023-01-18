from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True)
    description = Column(String)
    date_published = Column(DateTime)
    date_updated = Column(DateTime)
    is_public = Column(Boolean, default=True)
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="books")
    pages = relationship("Page", back_populates="book")
