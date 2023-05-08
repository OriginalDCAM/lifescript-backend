from sqlalchemy.orm import Session
from sqlalchemy import update
from src.books import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100) -> list[models.Book]:
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_title: str) -> models.Book:
    return db.query(models.Book).filter(models.Book.title == book_title).first()


def create_user_book(db: Session, book: schemas.BookCreate, user_id: int) -> models.Book:
    db_book = models.Book(**book.dict(), author_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_user_book(db: Session, book_id: int) -> models.Book:
    book = db.get(models.Book, book_id)
    if not book:
        return False
    db.delete(book)
    db.commit()
    return book

def update_user_book(db: Session, book_id: int, book: schemas.BookUpdate) -> models.Book:
    db.execute(update(models.Book).where(
        models.Book.id == book_id).values(**book.dict()))
    db.commit()
    return db.get(models.Book, book_id)
