import pytest
from src.phone import Phone


@pytest.fixture
def test_phone():
    return Phone("Самсунг", 30000, 30, 2)


@pytest.fixture
def test_phone_2():
    return Phone("Нокиа", 5000, 5, 1)


def test_number_of_sim_set(test_phone):
    """При вызове name происходит смена количества симок экземпляра, при этом,
    если количество меньше 0 или не целое, то вызывается ошибка"""
    test_phone.number_of_sim = 1
    assert test_phone.number_of_sim == 1
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0.1
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0


def test_repr(test_phone):
    """При вызове repr выводится информация для разработчиков"""
    assert repr(test_phone) == "Phone('Самсунг', 30000, 30, 2)"


def test_str(test_phone):
    """При вызове str выводится информация для пользователей в виде названия телефона"""
    assert str(test_phone) == "Самсунг"


def test_add(test_phone, test_phone_2):
    """При сложении возвращается общее количество товаров, при этом
    сложение происходит только объектов Phone и дочерних от них"""
    assert test_phone + test_phone_2 == 35
    with pytest.raises(ValueError):
        test_phone + 2
