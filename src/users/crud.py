from sqlalchemy.orm import Session
from sqlalchemy import update
from src.users import models, schemas
from src.helpers.hashing import Hasher


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = Hasher.get_password_hash(user.password)
    db_user = models.User(
        email=user.email, username=user.username, hashed_password=hashed_password, first_name=user.first_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# TODO: ADD FUNCTIONS FOR UPDATING A USER, SOFTDELETING A USER


def update_user(db: Session, user_input: schemas.UserUpdate, user_id: int):
    test = db.execute(update(models.User).where(
        models.User.id == user_id).values(first_name=user_input.first_name, username=user_input.username, email=user_input.email))
    user = db.get(models.User, user_id)
    return user


def delete_user(db: Session, user: schemas.User, user_id: int):
    user = db.get(models.User, user_id)
    if not user:
        return False
    db.delete(user)
    db.commit()
    return True
