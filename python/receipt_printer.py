from model_objects import ProductUnit

class ReceiptPrinter:
    def __init__(self, columns=40):
        self.columns = columns

    def print_receipt(self, receipt):
        result = ""
        result += self.print_items(receipt)
        result += self.print_discounts(receipt)
        result += "\n"
        result += self.print_total(receipt)
        return str(result)

    def print_items(self, receipt):
        items_text = ""
        for item in receipt.items:
            items_text += self.print_receipt_item(item)
        return items_text

    def print_receipt_item(self, item):
        total_price_printed = self.print_price(item.total_price)
        name = item.product.name
        line = self.format_line_with_whitespace(name, total_price_printed)
        if item.quantity != 1:
            line += f"  {self.print_price(item.price)} * {self.print_quantity(item)}\n"
        return line

    def format_line_with_whitespace(self, name, value):
        line = name.ljust(self.columns - len(value)) + value + "\n"
        return line

    def print_price(self, price):
        return "%.2f" % price

    def print_quantity(self, item):
        if item.product.unit == ProductUnit.EACH:
            return str(item.quantity)
        else:
            return '%.3f' % item.quantity

    def print_discounts(self, receipt):
        discounts_text = ""
        for discount in receipt.discounts:
            discounts_text += self.print_discount(discount)
        return discounts_text

    def print_discount(self, discount):
        name = f"{discount.description} ({discount.product.name})"
        value = self.print_price(discount.discount_amount)
        return self.format_line_with_whitespace(name, value)

    def print_total(self, receipt):
        name = "Total: "
        value = self.print_price(receipt.total_price())
        return self.format_line_with_whitespace(name, value)
