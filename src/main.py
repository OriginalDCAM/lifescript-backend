from fastapi import FastAPI
from .routers import books, pages, users

app = FastAPI()

app.include_router(books.router)
app.include_router(pages.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Hallo World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
