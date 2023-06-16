import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

from src.main import app
from src.database import Base, get_db
from src.users.crud import get_users, get_current_user


load_dotenv(dotenv_path=".env")

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@localhost:{os.getenv('POSTGRES_TEST_PORT')}/{os.getenv('POSTGRES_TEST_DB')}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

PAYLOAD = [{"first_name": "Test","last_name": "Test", "username": "testuser", "email": "testuser@test.com", "password": "thisisatestpassword"}, {
        "first_name": "Jake", "last_name": "Baker", "username": "JakeUser", "email": "jakebaker@test.com", "password": "thisisatestpassword"}]

PAYLOAD_LOGIN = {"email": PAYLOAD[0]["email"], "password": PAYLOAD[0]["password"]}


@pytest.fixture(autouse=True)
def create_user(test_db):
    # Make a request to create a user
    for data in PAYLOAD:
        response = client.post("/api/v1/users/", json=data)
    assert response.status_code == 201

def test_login_user():
    # Make a request to login a user with an existing email
    response = client.post("/api/v1/users/login", json=PAYLOAD_LOGIN)
    assert response.status_code == 200

    access_token = response.json()["access_token"]
    token_type = response.json()["token_type"]
    assert access_token is not None
    assert token_type == "bearer"

    response = client.post("/api/v1/users/validate_token", json={"access_token": access_token, "token_type": token_type})
    assert response.status_code == 200


def test_get_all_users():
 # Make a request to get all users
    response = client.get("/api/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["email"] == PAYLOAD[0]["email"]

def test_get_user_by_id():
    # Make a request to get a user by id
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    assert response.json() == {
    "first_name": PAYLOAD[0]['first_name'], "last_name": PAYLOAD[0]['last_name'],
    "username": PAYLOAD[0]['username'], "email": PAYLOAD[0]['email'],
    "id": 1, "is_active": True, "books": []}

def test_get_all_books():
    # Make a request to get books by user id
    response = client.get("/api/v1/books/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_book():
    # Make a request to create a book
    response = client.post(f"/api/v1/books/create_book/1",json={
        "title": "Test Book", "description": "A beautiful test Book"})
    assert response.status_code == 201
    assert response.json() == {
        "title": "Test Book",
        "description": "A beautiful test Book",
        "id": 1, "author_id": 1, "is_public":True,
        "pages": []}
