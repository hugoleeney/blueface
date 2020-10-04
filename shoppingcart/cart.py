import typing
from collections import OrderedDict

from . import abc


class NoSuchCurrencyException(Exception):
    pass


EUR_ONLY = {
    "eur": 1
}


EUR_SYMBOL_ONLY = {
    "eur": "€"
}


class FXDict(object):

    def __init__(self, rates=EUR_ONLY, symbols=EUR_SYMBOL_ONLY):
        self.rates = rates
        self.symbols = symbols

    def convert(self, amount, currency):
        if currency not in self.rates:
            raise NoSuchCurrencyException()
        else:
            converted = (amount *self.rates[currency])
            rounded = round(converted, 2)
            return rounded if rounded <= converted else rounded + 0.01

    def symbol(self, currency):
        if currency not in self.rates:
            raise NoSuchCurrencyException()
        else:
            return self.symbols[currency]


class ShoppingCart(abc.ShoppingCart):

    def __init__(self, price_store, fx=FXDict()):
        self._items = OrderedDict()
        self.price_store = price_store
        self.fx = fx

    def add_item(self, product_code: str, quantity: int):
        if product_code not in self._items:
            self._items[product_code] = quantity
        else:
            q = self._items[product_code]
            self._items[product_code] = q + quantity

    def print_receipt(self, currency: str="eur") -> typing.List[str]:
        lines = []
        total = 0
        for item in self._items.items():
            price = self.price_store.get_product_price(item[0]) * item[1]
            price = self.fx.convert(price, currency)
            total += price
            symbol = self.fx.symbol(currency)
            price_string = "%s%.2f" % (symbol, price)
            lines.append(item[0] + " - " + str(item[1]) + ' - ' + price_string)
        lines.append("Total - "+ "%s%.2f" % (symbol,total))
        return lines
