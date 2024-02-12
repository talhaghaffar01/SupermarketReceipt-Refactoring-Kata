class SupermarketCatalog:

    def add_product(self, product, price):
        """
        Add a product to the catalog with its corresponding price.

        This method should not be called directly from unit tests as it accesses the database.
        """
        raise Exception("Cannot be called from a unit test - it accesses the database")

    def unit_price(self, product):
        """
        Retrieve the unit price of a product from the catalog.

        This method should not be called directly from unit tests as it accesses the database.
        """
        raise Exception("Cannot be called from a unit test - it accesses the database")
