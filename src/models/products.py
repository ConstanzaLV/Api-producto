from sqlalchemy import Column, Integer, String, Float
from src.db.database import Base



class Product(Base):
    __tablename__='products'

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=True)
