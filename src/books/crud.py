from sqlalchemy.orm import Session
from src.books import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_user_book(db: Session, book: schemas.BookCreate, user_id: int):
    db_book = models.Book(**book.dict(), author_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_user_book(db: Session, book: schemas.Book):
    db_book = db.query(models.Book).where(book_id=book)
    return
