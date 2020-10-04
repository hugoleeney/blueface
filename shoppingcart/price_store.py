import json


class PriceStoreCode(object):

    def __init__(self):
        pass

    def get_product_price(self, product_code: str) -> float:
        price = 0.0

        if product_code == 'apple':
            price = 1.0

        elif product_code == 'banana':
            price = 1.1

        elif product_code == 'kiwi':
            price = 3.0

        elif product_code == 'pear':
            price = 2.0

        elif product_code == 'orange':
            price = 1.5

        return price


class NoPriceForProductException(Exception):
    pass


class PriceStoreDict(object):

    def __init__(self, data):
        self.data = data

    def get_product_price(self, product_code: str) -> float:
        if product_code not in self.data:
            raise NoPriceForProductException(product_code)
        else:
            return self.data[product_code]


class PriceStoreJson(PriceStoreDict):

    def __init__(self, json_string):
        self.data = json.loads(json_string)


class PriceStoreJsonFS(PriceStoreJson):

    def __init__(self, fs, filename):
        json_file = fs.open(filename, 'r')
        json_string = json_file.read()
        self.data = json.loads(json_string)