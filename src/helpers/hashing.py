import os
from datetime import datetime, timedelta

from passlib.context import CryptContext
from typing import Union, Any
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
JWT_REFRESH_SECRET_KEY = os.getenv('JWT_REFRESH_SECRET_KEY')

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_content.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: Union[str, Any]) -> str:
        return pwd_content.hash(password)

    @staticmethod
    def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow(
            ) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {"exp": expires_delta, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
        return encoded_jwt
