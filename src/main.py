from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from src.books.router import router as books_router
from src.users.router import router as users_router

app = FastAPI()

app.include_router(books_router)
app.include_router(users_router)
