from fastapi import APIRouter

router = APIRouter(
    prefix='/book/{name}',
    tags=['pages']
)


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



