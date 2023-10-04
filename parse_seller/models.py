from pydantic import BaseModel, field_validator


class Item(BaseModel):
    id: int
    name: str
    salePriceU: float
    brand: str
    feedbacks: int
    reviewRating: float
    sale: int
    volume: int
    supplierId: int
    pics: int
    image_links: str = None

    @field_validator('salePriceU')
    def convert_sale_price(cls, sale_price: int) -> float:
        if sale_price:
            return sale_price / 100


class Items(BaseModel):
    products: list[Item]