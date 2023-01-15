from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from src.books import crud, schemas

from src.database import get_db

router = APIRouter(
    prefix='/api/v1/books',
    tags=['books']
)


@router.post("/create_book/{user_id}", response_model=schemas.Book)
def create_book_for_user(user_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_user_book(db=db, book=book, user_id=user_id)


@router.get("/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books
