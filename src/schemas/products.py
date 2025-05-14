from typing import Optional
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = Field(default=None,description="Nombre completo del usuario")


class UpdateProduct(BaseModel):
    name: Optional[str] = Field(None)
    price: Optional[float] = Field(None)
    description: Optional[str] = Field(None)
