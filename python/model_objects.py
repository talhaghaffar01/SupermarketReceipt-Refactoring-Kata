from enum import Enum


class ProductUnit(Enum):
    EACH = 1
    KILO = 2
    LITER = 3
    DOZEN = 4


class SpecialOfferType(Enum):
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4


class Product:
    """Represents a product with a name and unit."""

    def __init__(self, name: str, unit: ProductUnit):
        self.name = name
        self.unit = unit


class ProductQuantity:
    """Represents the quantity of a product."""

    def __init__(self, product: Product, quantity: float):
        self.product = product
        self.quantity = quantity


class Offer:
    """Represents a special offer for a product."""

    def __init__(self, offer_type: SpecialOfferType, product: Product, argument: float):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument


class Discount:
    """Represents a discount for a product."""

    def __init__(self, product: Product, description: str, discount_amount: float):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount
