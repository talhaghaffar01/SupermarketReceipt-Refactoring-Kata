from enum import Enum

class Product:
    """
    Represents a product in the supermarket.
    
    Attributes:
    - name: The name of the product.
    - unit: The unit of measurement for the product (e.g., EACH, KILO).
    """
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit


class ProductQuantity:
    """
    Represents a quantity of a specific product.
    
    Attributes:
    - product: The product object.
    - quantity: The quantity of the product.
    """
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class ProductUnit(Enum):
    """
    Enumeration of product units.
    """
    EACH = 1
    KILO = 2


class SpecialOfferType(Enum):
    """
    Enumeration of special offer types.
    """
    THREE_FOR_TWO = 1
    TEN_PERCENT_DISCOUNT = 2
    TWO_FOR_AMOUNT = 3
    FIVE_FOR_AMOUNT = 4


class Offer:
    """
    Represents a special offer on a product.
    
    Attributes:
    - offer_type: The type of the special offer.
    - product: The product to which the offer applies.
    - argument: The argument for the offer.
    """
    def __init__(self, offer_type, product, argument):
        self.offer_type = offer_type
        self.product = product
        self.argument = argument


class Discount:
    """
    Represents a discount on a product.
    
    Attributes:
    - product: The product to which the discount applies.
    - description: A description of the discount.
    - discount_amount: The amount of discount.
    """
    def __init__(self, product, description, discount_amount):
        self.product = product
        self.description = description
        self.discount_amount = discount_amount
