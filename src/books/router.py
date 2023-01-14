from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

books = APIRouter(
    prefix='/books',
    tags=['books']
)


@books.get('/')
async def get_all_books():
    return 'All Books'


@books.get('{name}')
async def get_book():
    return 'Book'


@books.post('/create')
async def create_book():
    pass


@books.delete('/{id}')
async def delete_book():
    pass


@books.put('/{id}')
async def update_book():
    pass


@books.get('/page/{id}')
async def get_book_page():
    return 'This is awesome'


@books.post('/create')
async def create_book_page():
    pass


@books.delete('/{id}')
async def delete_book_page():
    pass


@books.put('/{id}')
async def update_book_page():
    pass
