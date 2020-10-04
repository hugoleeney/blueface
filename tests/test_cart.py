from shoppingcart.cart import ShoppingCart, FXDict
from shoppingcart.price_store import PriceStoreCode, PriceStoreDict


def test_add_different_items():
    cart = ShoppingCart(PriceStoreCode())
    cart.add_item("banana", 1)
    cart.add_item("pear", 1)
    cart.add_item("kiwi", 1)
    cart.add_item("orange", 1)
    cart.add_item("apple", 1)
    cart.add_item("apple", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - €1.10"
    assert receipt[1] == "pear - 1 - €2.00"
    assert receipt[2] == "kiwi - 1 - €3.00"
    assert receipt[3] == "orange - 1 - €1.50"
    assert receipt[4] == "apple - 2 - €2.00"
    assert receipt[5] == "Total - €9.60"


FX_RATES = {
    'usd': 1.21
}


FX_SYMBOLS = {
    'usd': '$'
}


def test_cart_in_dollars():
    cart = ShoppingCart(PriceStoreCode(), FXDict(FX_RATES, FX_SYMBOLS))
    cart.add_item("banana", 1)
    receipt = cart.print_receipt('usd')
    assert receipt[0] == "banana - 1 - $1.33"
    assert receipt[1] == "Total - $1.33"

