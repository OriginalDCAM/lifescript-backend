from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/books',
    tags=['books']
)


@router.get('/')
async def get_all_books():
    return 'All Books'


@router.get('{name}')
async def get_book():
    return 'Book'


@router.post('/create')
async def create_book():
    pass


@router.delete('/{id}')
async def delete_book():
    pass


@router.put('/{id}')
async def update_book():
    pass


@router.get('/page/{id}')
async def get_book_page():
    return 'This is awesome'


@router.post('/create')
async def create_book_page():
    pass


@router.delete('/{id}')
async def delete_book_page():
    pass


@router.put('/{id}')
async def update_book_page():
    pass
