class ReceiptItem:
    """
    Represents an item in a receipt.
    
    Attributes:
    - product: The product associated with the receipt item.
    - quantity: The quantity of the product.
    - price: The price per unit of the product.
    - total_price: The total price of the receipt item.
    """
    def __init__(self, product, quantity, price, total_price):
        self.product = product
        self.quantity = quantity
        self.price = price
        self.total_price = total_price


class Receipt:
    """
    Represents a receipt.
    
    Attributes:
    - _items: A list of ReceiptItem objects representing items in the receipt.
    - _discounts: A list of Discount objects representing discounts applied to the receipt.
    """
    def __init__(self):
        self._items = []
        self._discounts = []

    def total_price(self):
        """
        Calculates the total price of the receipt, including items and discounts.
        
        Returns:
        - The total price of the receipt.
        """
        total = 0
        for item in self.items:
            total += item.total_price
        for discount in self.discounts:
            total += discount.discount_amount
        return total

    def add_product(self, product, quantity, price, total_price):
        """
        Adds a product to the receipt.
        
        Parameters:
        - product: The product to add.
        - quantity: The quantity of the product.
        - price: The price per unit of the product.
        - total_price: The total price of the product.
        """
        self._items.append(ReceiptItem(product, quantity, price, total_price))

    def add_discount(self, discount):
        """
        Adds a discount to the receipt.
        
        Parameters:
        - discount: The discount to add.
        """
        self._discounts.append(discount)

    @property
    def items(self):
        """
        Returns:
        - A copy of the list of ReceiptItem objects representing items in the receipt.
        """
        return self._items[:]

    @property
    def discounts(self):
        """
        Returns:
        - A copy of the list of Discount objects representing discounts applied to the receipt.
        """
        return self._discounts[:]
