from fastapi import APIRouter

router = APIRouter()


@router.get('/login/', tags=['users'])
async def login():
    return 'login'


@router.get('/register/', tags=["users"])
async def register():
    return 'register'


@router.post('login', tags=['users'])
async def login():
    return 'test'


@router.post('register', tags=['users'])
async def register():
    return 'test'
