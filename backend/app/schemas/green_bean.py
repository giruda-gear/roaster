from decimal import Decimal
from pydantic import BaseModel, ConfigDict


class GreenBeanCreate(BaseModel):
    name: str
    origin: str
    region: str
    variety: str
    process: str
    stock_kg: Decimal
    price_per_kg: Decimal
    description: str | None = None


class GreenBeanResponse(GreenBeanCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
