from fastapi import APIRouter

router = APIRouter(
    prefix='/books',
    tags=['books']
)


@router.get('/')
async def get_all_books():
    return 'All Troll'


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
