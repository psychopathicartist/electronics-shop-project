from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона как товара в магазине
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone.

        :param name: Название телефона
        :param price: Цена за единицу товара
        :param quantity: Количество товара в магазине
        :param number_of_sim: Количество  поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователя
        """
        return f'{self.name}'

    def __add__(self, other):
        """
        Возвращает сложение экземпляров класса Phone и Item по количеству товара в магазин
        """
        if not isinstance(other, Phone):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        """
        Возвращает название товара
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Метод срабатывает при операции присваивания названия товара
        и оставляет длину товара не более 10 символов
        """
        if type(number_of_sim) == int and number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
