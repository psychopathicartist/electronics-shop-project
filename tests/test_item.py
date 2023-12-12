import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("Холодильник", 40000, 10)


def test_calculate_total_price(test_item):
    """При вызове calculate_total_price возвращает значение 400000
    при цене 40000 и количестве 10"""
    assert test_item.calculate_total_price() == 400000


def test_apply_discount(test_item):
    """При вызове apply_discount обновляет цену товара с учетом скидки 40%,
    цена становится равной 24000.0, в формате float"""
    Item.pay_rate = 0.6
    test_item.apply_discount()
    assert test_item.price == 24000.0
