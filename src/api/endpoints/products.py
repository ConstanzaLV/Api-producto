from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.dependency import get_db
from src import crud, schemas

router=APIRouter()


@router.get("", summary='Obtener todos los productos')
def get_products(db: Session = Depends(get_db)):
    return crud.get_products(db)


@router.get("/{id}", summary='Obener un producto')
def get_product(id: int, db: Session = Depends(get_db)):
    return crud.get_product_by_id(id, db)

@router.post("", summary='Crear un producto')
def create_product(product: schemas.Product, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.put("/{id}", summary='Actualziar un producto')
def update_product(id: int, product: schemas.UpdateProduct, db: Session = Depends(get_db)):
    return crud.update_product(db, id, product)


@router.delete("/{id}", summary='Borrar un producto')
def delete_product(id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, id)