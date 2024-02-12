import pytest

from model_objects import Product, SpecialOfferType, ProductUnit
from shopping_cart import ShoppingCart
from teller import Teller
from tests.fake_catalog import FakeCatalog


def test_ten_percent_discount():
    catalog = FakeCatalog()
    toothbrush = Product("toothbrush", ProductUnit.EACH)
    catalog.add_product(toothbrush, 0.99)

    apples = Product("apples", ProductUnit.KILO)
    catalog.add_product(apples, 1.99)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TEN_PERCENT_DISCOUNT, toothbrush, 10.0)

    cart = ShoppingCart()
    cart.add_item_quantity(apples, 2.5)

    receipt = teller.checks_out_articles_from(cart)

    assert 4.975 == pytest.approx(receipt.total_price(), 0.01)
    assert [] == receipt.discounts
    assert 1 == len(receipt.items)
    receipt_item = receipt.items[0]
    assert apples == receipt_item.product
    assert 1.99 == receipt_item.price
    assert 2.5 * 1.99 == pytest.approx(receipt_item.total_price, 0.01)
    assert 2.5 == receipt_item.quantity


def test_two_for_amount_discount():
    catalog = FakeCatalog()
    cereal = Product("cereal", ProductUnit.EACH)
    catalog.add_product(cereal, 2.50)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, cereal, 4.00)

    cart = ShoppingCart()
    cart.add_item_quantity(cereal, 4)

    receipt = teller.checks_out_articles_from(cart)
    expected_total_price = 8.00

    assert expected_total_price == pytest.approx(receipt.total_price(), 0.01)


def test_five_for_amount_discount():
    catalog = FakeCatalog()
    cookies = Product("cookies", ProductUnit.EACH)
    catalog.add_product(cookies, 1.00)

    teller = Teller(catalog)
    teller.add_special_offer(SpecialOfferType.FIVE_FOR_AMOUNT, cookies, 3.00)

    cart = ShoppingCart()
    cart.add_item_quantity(cookies, 8)

    receipt = teller.checks_out_articles_from(cart)
    regular_price = 8 * 1.00
    discount_amount = 1.00 * 2
    expected_total_price = regular_price - discount_amount

    assert expected_total_price == pytest.approx(receipt.total_price(), 0.01)


def test_non_discounted_items():
    catalog = FakeCatalog()
    apple = Product("apple", ProductUnit.EACH)
    catalog.add_product(apple, 1.50)

    banana = Product("banana", ProductUnit.EACH)
    catalog.add_product(banana, 0.75)

    orange = Product("orange", ProductUnit.EACH)
    catalog.add_product(orange, 1.20)
    teller = Teller(catalog)
    cart = ShoppingCart()
    cart.add_item_quantity(apple, 2)
    cart.add_item_quantity(banana, 3)
    cart.add_item_quantity(orange, 1)
    receipt = teller.checks_out_articles_from(cart)
    expected_total_price = (2 * 1.50) + (3 * 0.75) + (1 * 1.20)

    assert expected_total_price == pytest.approx(receipt.total_price(), 0.01)

def test_different_quantities():
    catalog = FakeCatalog()
    milk = Product("milk", ProductUnit.LITER)
    catalog.add_product(milk, 1.80)

    bread = Product("bread", ProductUnit.EACH)
    catalog.add_product(bread, 1.20)

    eggs = Product("eggs", ProductUnit.DOZEN)
    catalog.add_product(eggs, 3.50)

    teller = Teller(catalog)

    teller.add_special_offer(SpecialOfferType.TWO_FOR_AMOUNT, bread, 2.00)
    teller.add_special_offer(SpecialOfferType.THREE_FOR_TWO, eggs, None)

    cart = ShoppingCart()

    cart.add_item_quantity(milk, 2.5)  # 2.5 liters of milk
    cart.add_item_quantity(bread, 3)    # 3 loaves of bread
    cart.add_item_quantity(eggs, 2)     # 2 dozens of eggs

    receipt = teller.checks_out_articles_from(cart)

    expected_total_price = 4.50 + 3.60 + 7.00
    tolerance = 0.2

    assert expected_total_price == pytest.approx(receipt.total_price(), tolerance)
