import logging
from fastapi import Depends, HTTPException, status
from typing import Optional, Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from sqlalchemy import update
from src.users import models, schemas
from src.helpers.hashing import Hasher
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
ALGORITHM = "HS256"


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=hashed_password, first_name=user.first_name, last_name=user.last_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_input: schemas.UserUpdate, user_id: int):
    test = db.execute(update(models.User).where(
        models.User.id == user_id).values(first_name=user_input.first_name, last_name=user_input.last_name, username=user_input.username, email=user_input.email))
    user = db.get(models.User, user_id)
    return user


def delete_user(db: Session, user: schemas.User, user_id: int):
    user = db.get(models.User, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True


def user_login(db: Session, user_input: schemas.UserLogin):
    user = db.query(models.User).filter(
        models.User.email == user_input.email).first()

    # Checks if user exists in the database if not return the empty user
    if user is None:
        return None

    check_if_passwords_match = Hasher.verify_password(
        user_input.password, user.hashed_password)

    # Checks if the passwords dont match return none value
    if not check_if_passwords_match:
        return None

    return user


def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token.access_token, os.getenv(
            'JWT_SECRET_KEY'), algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            logging.warning("Email not found")
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        logging.error("JWT Error")
        raise credentials_exception
    user = get_user_by_email(db, email=token_data.email)
    if user is None:
        logging.error(f"User not found{token_data.email}")
        raise credentials_exception
    return user
