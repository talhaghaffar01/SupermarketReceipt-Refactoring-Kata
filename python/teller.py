from model_objects import Offer
from receipt import Receipt

class Teller:
    def __init__(self, catalog):
        self.catalog = catalog
        self.offers = {}

    def add_special_offer(self, offer_type, product, argument):
        """
        Adds a special offer to the teller's list of offers.

        Parameters:
        - offer_type: Type of special offer.
        - product: The product to which the offer applies.
        - argument: Additional argument (e.g., discount percentage, price) for the offer.
        """
        self.offers[product] = Offer(offer_type, product, argument)

    def checks_out_articles_from(self, the_cart):
        """
        Handles checkout operations by generating a receipt.

        Parameters:
        - the_cart: The shopping cart containing items to be checked out.

        Returns:
        - Receipt: The generated receipt.
        """
        if not the_cart:
            raise ValueError("The shopping cart is empty.")

        receipt = Receipt()
        product_quantities = the_cart.items

        for pq in product_quantities:
            p = pq.product
            quantity = pq.quantity
            unit_price = self.catalog.unit_price(p)
            price = quantity * unit_price
            receipt.add_product(p, quantity, unit_price, price)

        self.apply_special_offers(receipt, the_cart)

        return receipt

    def apply_special_offers(self, receipt, the_cart):
        """
        Applies special offers to items in the shopping cart.

        Parameters:
        - receipt: The receipt to which discounts will be applied.
        - the_cart: The shopping cart containing items.
        """
        if not self.offers:
            return

        the_cart.handle_offers(receipt, self.offers, self.catalog)
