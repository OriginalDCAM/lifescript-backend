from sqlalchemy.orm import Session
from src.books import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_user_book(db: Session, item: schemas.BookCreate, user_id: int):
    db_book = models.Integer(**item-dict(), author_id=user_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
