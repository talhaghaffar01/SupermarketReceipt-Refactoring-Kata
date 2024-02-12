from model_objects import ProductUnit


class ReceiptPrinter:
    """Prints the receipt for the supermarket."""

    def __init__(self, columns=40):
        self.columns = columns

    def print_receipt(self, receipt):
        """Prints the receipt items and discounts."""
        result = ""
        for item in receipt.items:
            receipt_item = self.print_receipt_item(item)
            result += receipt_item

        for discount in receipt.discounts:
            discount_presentation = self.print_discount(discount)
            result += discount_presentation

        result += "\n"
        result += self.present_total(receipt)
        return str(result)

    def print_receipt_item(self, item):
        """Prints an individual receipt item."""
        total_price_printed = self.print_price(item.total_price)
        name = item.product.name
        line = f"{name.ljust(self.columns - 10)} {total_price_printed}\n"
        if item.quantity != 1:
            line += f"  {self.print_price(item.price)} * {self.print_quantity(item)}\n"
        return line

    def print_price(self, price):
        """Formats the price."""
        return "%.2f" % price

    def print_quantity(self, item):
        """Formats the quantity."""
        if item.product.unit == ProductUnit.EACH:
            return str(item.quantity)
        else:
            return '%.3f' % item.quantity

    def print_discount(self, discount):
        """Prints the discount information."""
        name = f"{discount.description} ({discount.product.name})"
        value = self.print_price(discount.discount_amount)
        return f"{name.ljust(self.columns - 10)} {value}\n"

    def present_total(self, receipt):
        """Presents the total price of the receipt."""
        name = "Total: "
        value = self.print_price(receipt.total_price())
        return f"{name.ljust(self.columns - 10)} {value}\n"
