from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session

from src.routes import books, pages, users
from src import schemas, models, crud
from src.database import get_db


app = FastAPI()

app.include_router(books.router)
app.include_router(pages.router)
app.include_router(users.router)


@app.get("/test/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users
