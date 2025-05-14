from sqlalchemy.orm import Session
from src import models, schemas


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()


def create_product(db: Session, user: schemas.products):
    db_product = models.Product(**user.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, user_id: int, user_data: schemas.UpdateProduct):
    db_product = db.query(models.Product).filter(models.Product.id == user_id).first()
    if not db_product:
        return None
    for key, value in user_data.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, user_id: int):
    db_product = db.query(models.Product).filter(models.Product.id == user_id).first()
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
