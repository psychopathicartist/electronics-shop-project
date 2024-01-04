import csv
import os.path


class InstantiateCSVError(Exception):
    """
    Класс исключения при отсутствии каких-либо данных в файле
    """
    def __init__(self):
        self.message = 'Файл item.csv поврежден.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        super().__init__()

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователя
        """
        return f'{self.__name}'

    def __add__(self, other):
        """
        Возвращает сложение экземпляров класса Phone и Item по количеству товара в магазин
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename='../src/items.csv'):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        cls.all = []
        if not os.path.exists(filename):
            raise FileNotFoundError('Отсутствует файл item.csv.')
        else:
            with open(filename, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if 'name' not in row or 'price' not in row or 'quantity' not in row:
                        raise InstantiateCSVError
                    else:
                        svc_name = row['name']
                        svc_price = float(row['price'])
                        svc_quantity = int(row['quantity'])
                        cls(svc_name, svc_price, svc_quantity)

    @staticmethod
    def string_to_number(str_number):
        """
        Возвращает целое число из числа-строки
        """
        number = float(str_number)
        return int(number)

    @property
    def name(self):
        """
        Возвращает название товара
        """
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Метод срабатывает при операции присваивания названия товара
        и оставляет длину товара не более 10 символов
        """
        self.__name = new_name[:10]
