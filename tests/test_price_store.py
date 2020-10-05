import json
import fs as fs
import pytest
from moneyed import Money, USD

from shoppingcart.price_store import NoPriceForProductException, PriceStoreDict, PriceStoreJson, PriceStoreJsonFS


prices = {"apple": 1.0, "pear": 2.0}
prices_json_string = json.dumps(prices)

@pytest.fixture
def ps(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def price_store_dict():
    return PriceStoreDict(prices)


@pytest.fixture
def price_store_json():
    return PriceStoreJson(prices_json_string)


@pytest.fixture
def price_store_fs():
    inmemfs = fs.open_fs('mem://')
    file_name = 'prices.json'
    prices_file = inmemfs.open(file_name, 'x')
    prices_file.write(prices_json_string)
    prices_file.close()
    return PriceStoreJsonFS(inmemfs, file_name)


@pytest.mark.parametrize("ps", ['price_store_dict', 'price_store_json', 'price_store_fs'], indirect=True)
def test_get_product_price(ps):
    assert ps.get_product_price("apple") == Money(1.0, 'eur')

    with pytest.raises(NoPriceForProductException):
        assert ps.get_product_price("tomato")
