from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from src.books import crud, schemas
from src.pages import crud, schemas

from src.database import get_db

router = APIRouter(
    prefix='/api/v1/pages',
    tags=['pages']
)



@router.get("/{page_id}", response_model=schemas.Page)
def read_page(page_id: int, db: Session = Depends(get_db)):
    page = crud.get_page(db, page_id=page_id)
    if page is None:
        raise HTTPException(status_code=404, detail="Page not found")
    return page