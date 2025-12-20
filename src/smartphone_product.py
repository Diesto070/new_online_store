from typing import Any

from src.product_category import Product


class Smartphone(Product):
    """Класс, представляющий смартфон как товар в магазине.
    Наследует все основные свойства от класса Product и добавляет
    специфические характеристики для смартфонов.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        """Инициализирует объект смартфона.
        Args:
            name: Название смартфона
            description: Описание характеристик смартфона
            price: Цена смартфона в рублях
            quantity: Количество единиц товара на складе
            efficiency: Производительность процессора (в ГГц или условных единицах)
            model: Модель смартфона
            memory: Объем внутренней памяти в ГБ
            color: Цвет корпуса смартфона
        """
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: Any) -> float:
        """Складывает общую стоимость двух партий смартфонов.
        Позволяет вычислять суммарную стоимость товаров на складе
        путем умножения цены на количество для каждого объекта и сложения результатов.

            Args:
                other: Другой объект Smartphone для сложения

            Returns:
                float: Суммарная стоимость товаров (цена × количество)

            Raises:
                TypeError: Если other не является объектом Smartphone"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
