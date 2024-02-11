class SupermarketCatalog:
    def __init__(self, database=None):
        self._database = database

    def add_product(self, product, price):
        if self._database is None:
            raise DatabaseAccessException("Database access is not available for unit tests")
        self._database.add_product(product, price)

    def unit_price(self, product):
        if self._database is None:
            raise DatabaseAccessException("Database access is not available for unit tests")
        return self._database.unit_price(product)


class DatabaseAccessException(Exception):
    pass
