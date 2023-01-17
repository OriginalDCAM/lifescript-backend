from passlib.context import CryptContext

pwd_content = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher():
    @staticmethod
    def verify_password(plain_password, hashed_password):
        return pwd_content.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password):
        return pwd_content.hash(password)
