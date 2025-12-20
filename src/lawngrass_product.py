from typing import Any

from src.product_category import Product


class LawnGrass(Product):
    """Класс, представляющий газонную траву как товар в магазине.
    Наследует все основные свойства от класса Product и добавляет
    специфические характеристики для травы."""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        """Инициализирует объект газонной травы."""
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other: Any) -> float:
        """Складывает общую стоимость двух партий газонной травы.
        Args:
            other: Другой объект LawnGrass для сложения
        Returns:
            float: Суммарная стоимость товаров (цена × количество)
        Raises:
            TypeError: Если other не является объектом LawnGrass
        """
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
