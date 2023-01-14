from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from src.books.router import books
from src.users.router import users

app = FastAPI()

app.include_router(books)
app.include_router(users)
