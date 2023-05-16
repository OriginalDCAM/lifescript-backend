from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.helpers.hashing import Hasher

from src.users import crud, schemas

from src.database import get_db

router = APIRouter(
    prefix='/api/v1/users',
    tags=['users']
)


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/login", response_model=schemas.UserToken)
def login_user(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.user_login(db=db, user_input=user)
    if db_user is None:
        raise HTTPException(
            status_code=404, detail="Invalid login or password.")
    token = Hasher.create_access_token(subject=db_user.email)
    print(db_user)
    return {"access_token": token, "token_type": "bearer", "first_name": db_user.first_name, "username": db_user.username, "email": db_user.email}


@router.put("/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user_input: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_input=user_input, user_id=user_id)

@router.post("/validate_token", response_model=schemas.User)
def read_users_me(token: schemas.Token, db: Session = Depends(get_db)):
    return crud.get_current_user(db=db, token=token)