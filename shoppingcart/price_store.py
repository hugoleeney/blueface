import json

from moneyed import Money, EUR


class PriceStoreCode(object):

    def __init__(self):
        pass

    def get_product_price(self, product_code: str) -> float:
        price = Money(0.0, EUR)

        if product_code == 'apple':
            price = Money(1.0, EUR)

        elif product_code == 'banana':
            price = Money(1.1, EUR)

        elif product_code == 'kiwi':
            price = Money(3.0, EUR)

        elif product_code == 'pear':
            price = Money(2.0, EUR)

        elif product_code == 'orange':
            price = Money(1.5, EUR)

        return price


class NoPriceForProductException(Exception):
    pass


class PriceStoreDict(object):

    def __init__(self, data):
        self.data = data
        for product, price in self.data.items():
            self.data[product] = Money(price, EUR)

    def get_product_price(self, product_code: str) -> float:
        if product_code not in self.data:
            raise NoPriceForProductException(product_code)
        else:
            return self.data[product_code]


class PriceStoreJson(PriceStoreDict):

    def __init__(self, json_string):
        data = json.loads(json_string)
        super(PriceStoreJson, self).__init__(data)


class PriceStoreJsonFS(PriceStoreJson):

    def __init__(self, fs, filename):
        json_file = fs.open(filename, 'r')
        json_string = json_file.read()
        super(PriceStoreJsonFS, self).__init__(json_string)

