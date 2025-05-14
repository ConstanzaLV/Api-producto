from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.dependency import get_db
from src import crud, schemas

router=APIRouter()


@router.get("")
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.post("")
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
    # return {"message":"hola"}  

@router.put("/{id}")
def update_product(id: int, product: schemas.UpdateProduct, db: Session = Depends(get_db)):
    return crud.update_product(db, id, product)


@router.delete("/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)