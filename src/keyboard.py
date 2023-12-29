from src.item import Item


class MixinKey:
    """
    Класс-миксин для хранения и изменения раскладки на клавиатуре.
    """
    def_language = 'EN'

    def __init__(self) -> None:
        """
        Создание экземпляра миксин-класса с языком по умолчанию 'EN'
        """
        self.__language = self.def_language

    def change_lang(self) -> None:
        """
        Меняет язык раскладки клавиатуры
        """
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'

    @property
    def language(self):
        """
        Возвращает язык раскладки клавиатуры
        """
        return self.__language


class Keyboard(Item, MixinKey):
    """
    Класс для представления клавиатуры в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса keyboard.

        :param name: Название клавиатуры.
        :param price: Цена за клавиатуру.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)

    def __repr__(self) -> str:
        """
        Возвращает информацию об объекте класса для разработчиков
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Возвращает информацию об объекте класса для пользователя
        """
        return f'{self.name}'
