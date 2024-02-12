from catalog import SupermarketCatalog
class FakeCatalog(SupermarketCatalog):
    def __init__(self):
        self.products = {}
        self.prices = {}

    def add_product(self, product, price):
        self.products[product.name] = product
        self.prices[product.name] = price

    def unit_price(self, product):
        return self.prices.get(product.name, 0.0)  # Return 0.0 if the product is not found
