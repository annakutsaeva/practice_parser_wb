#'id', 'название', 'цена', 'бренд', 'продаж', 'рейтинг', 'в наличии'
from pydantic import BaseModel, root_validator, model_validator

class Item(BaseModel):
    id: int
    name: str
    salePriceU: float
    brand: str
    sale: int
    rating: int
    volume: int

    @model_validator(mode='before')
    def convert_sale_price(cls, values: dict):
        sale_price = values.get("salePriceU")
        if sale_price:
            values["salePriceU"] = sale_price / 100
        return values

    """
    @root_validator(pre=True) #True чтобы сработал перед другими валидаторами
        def convert_sale_price(cls, values: dict):
            sale_price = values.get("salePriceU")
            if sale_price:
                values["salePriceU"] = sale_price/100
            return values
    """

class Items(BaseModel):
    products: list[Item]


