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


def test_string_to_number():
    """При вызове string_to_number преобразует число из формата str в формат int"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    """При вызове instantiate_from_csv происходить инициализация экземпляров класса
    из файла items.csv, тогда количество экземпляров класса равно 5"""
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_name_set(test_item):
    """При вызове name происходит смена имени экземпляра, при этом,
    если длина названия больше 10 символов, то лишнее отсекается"""
    test_item.name = 'Смартфон'
    assert test_item.name == 'Смартфон'
    test_item.name = 'Холодильник'
    assert test_item.name == 'Холодильни'
