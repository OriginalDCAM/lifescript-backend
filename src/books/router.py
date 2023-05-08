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
    book = crud.create_user_book(db=db, book=book, user_id=user_id)
    return book


@router.get("/", response_model=list[schemas.Book])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get("/{book_title}", response_model=schemas.Book)
def read_book(book_title: str, db: Session = Depends(get_db)):
    book = crud.get_book(db=db, book_title=book_title)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.delete("/delete_book/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    delete_book = crud.delete_user_book(db=db, book_id=book_id)
    if delete_book is False:
        raise HTTPException(status_code=404, detail="Book not found")
    return delete_book

@router.put("/update_book/{book_id}")
def update_book(book_id: int, user_input: schemas.BookUpdate, db: Session = Depends(get_db)):
    update_book = crud.update_user_book(db=db, book_id=book_id, book=user_input)
    if update_book is False:
        raise HTTPException(status_code=404, detail="Book not found")
    return update_book