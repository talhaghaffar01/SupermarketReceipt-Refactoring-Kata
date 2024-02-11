import math
from model_objects import ProductQuantity, SpecialOfferType, Discount


class ShoppingCart:
    def __init__(self):
        self._items = []
        self._product_quantities = {}

    @property
    def items(self):
        return self._items

    def add_item(self, product):
        """
        Adds an item to the shopping cart.
        """
        self.add_item_quantity(product, 1.0)

    @property
    def product_quantities(self):
        return self._product_quantities

    def add_item_quantity(self, product, quantity):
        """
        Adds a specific quantity of an item to the shopping cart.
        """
        self._items.append(ProductQuantity(product, quantity))
        if product in self._product_quantities:
            self._product_quantities[product] += quantity
        else:
            self._product_quantities[product] = quantity

    def handle_offers(self, receipt, offers, catalog):
        """
        Handles offers applied to items in the shopping cart.
        """
        for product, quantity in self._product_quantities.items():
            if product in offers:
                offer = offers[product]
                self.apply_offer(receipt, offer, product, quantity, catalog)

    def apply_offer(self, receipt, offer, product, quantity, catalog):
        """
        Applies a specific offer to items in the shopping cart.
        """
        unit_price = catalog.unit_price(product)
        quantity_as_int = int(quantity)
        discount = None
        x = 1

        if offer.offer_type == SpecialOfferType.THREE_FOR_TWO:
            x = 3
            if quantity_as_int >= 3:
                discount_amount = (quantity_as_int // 3) * 1 * unit_price
                discount = Discount(product, "3 for 2", -discount_amount)

        elif offer.offer_type == SpecialOfferType.TWO_FOR_AMOUNT:
            x = 2
            if quantity_as_int >= 2:
                total = offer.argument * (quantity_as_int // 2) + quantity_as_int % 2 * unit_price
                discount_amount = unit_price * quantity - total
                discount = Discount(product, f"2 for {offer.argument}", -discount_amount)

        elif offer.offer_type == SpecialOfferType.FIVE_FOR_AMOUNT:
            x = 5
            if quantity_as_int >= 5:
                discount_total = unit_price * quantity - (offer.argument * (quantity_as_int // 5) + quantity_as_int % 5 * unit_price)
                discount = Discount(product, f"5 for {offer.argument}", -discount_total)

        elif offer.offer_type == SpecialOfferType.TEN_PERCENT_DISCOUNT:
            discount_amount = quantity * unit_price * offer.argument / 100.0
            discount = Discount(product, f"{offer.argument}% off", -discount_amount)

        if discount:
            receipt.add_discount(discount)
