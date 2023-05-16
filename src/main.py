from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from src.books.router import router as books_router
from src.users.router import router as users_router
from src.pages.router import router as page_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:80"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="LifeScript API",
        version="1.0.0",
        description="API for LifeScript",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.include_router(books_router)
app.include_router(users_router)
app.include_router(page_router)

app.openapi = custom_openapi
