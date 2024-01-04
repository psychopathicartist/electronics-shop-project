import pytest
import os
from src.item import Item, InstantiateCSVError


items_file = 'C:/Users/Мария/PycharmProjects/electronics-shop-project/src/items.csv'
test_items_file = 'C:/Users/Мария/PycharmProjects/electronics-shop-project/tests/items_test.csv'


@pytest.fixture
def test_item():
    return Item("Холодильник", 40000, 10)


@pytest.fixture
def test_item_2():
    return Item("Микроволновка", 5000, 40)


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
    """При вызове instantiate_from_csv происходит инициализация экземпляров класса
    из файла items.csv, тогда количество экземпляров класса равно 5"""
    Item.instantiate_from_csv(items_file)
    assert len(Item.all) == 5


def test_instantiate_csv_error():
    """При вызове instantiate_from_csv от поврежденного файла
    возникает ошибка InstantiateCSVError"""
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(test_items_file)


def test_instantiate_csv_error_str():
    """При вызове str от экземпляра класса исключения InstantiateCSVError
     выводится текст ошибки 'Файл item.csv поврежден.'"""
    assert str(InstantiateCSVError()) == 'Файл item.csv поврежден.'


def test_file_not_find():
    """При вызове instantiate_from_csv от несуществующего файла
    возникает ошибка FileNotFoundError"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('file')


def test_name_set(test_item):
    """При вызове name происходит смена имени экземпляра, при этом,
    если длина названия больше 10 символов, то лишнее отсекается"""
    test_item.name = 'Смартфон'
    assert test_item.name == 'Смартфон'
    test_item.name = 'Холодильник'
    assert test_item.name == 'Холодильни'


def test_repr(test_item):
    """При вызове repr выводится информация для разработчиков"""
    assert repr(test_item) == "Item('Холодильник', 40000, 10)"


def test_str(test_item):
    """При вызове str выводится информация для пользователей в виде названия товара"""
    assert str(test_item) == "Холодильник"


def test_add(test_item, test_item_2):
    """При сложении возвращается общее количество товаров, при этом
    сложение происходит только объектов Item и дочерних от них"""
    assert test_item + test_item_2 == 50
    with pytest.raises(ValueError):
        test_item + 2
