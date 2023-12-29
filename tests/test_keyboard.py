import pytest
from src.keyboard import Keyboard, MixinKey


@pytest.fixture
def test_keyboard():
    return Keyboard("Логитек", 2000, 30)


def test_repr(test_keyboard):
    """При вызове repr выводится информация для разработчиков"""
    assert repr(test_keyboard) == "Keyboard('Логитек', 2000, 30)"


def test_str(test_keyboard):
    """При вызове str выводится информация для пользователей в виде названия клавиатуры"""
    assert str(test_keyboard) == "Логитек"


def test_language_get(test_keyboard):
    """При вызове name происходит смена количества симок экземпляра, при этом,
    если количество меньше 0 или не целое, то вызывается ошибка"""
    assert str(test_keyboard.language) == "EN"


def test_change_lang(test_keyboard):
    """При вызове change_lang происходит смена языка раскладки клавиатуры,
    если изначально язык был русским, он должен перейти на английский"""
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "RU"
    test_keyboard.change_lang()
    assert str(test_keyboard.language) == "EN"
