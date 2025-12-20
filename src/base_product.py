from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс, который становится родительским для класса продуктов."""

    def __init__(self, name: str, description: str, quantity: int) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового отображения продукта"""
        ...

    @property
    @abstractmethod
    def price(self) -> float:
        """Абстрактный геттер для цены продукта."""
        ...

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        """Абстрактный сеттер для цены продукта с проверкой."""
        ...

    @classmethod
    @abstractmethod
    def new_product(cls, *args: Any, **kwargs: Any) -> "BaseProduct":
        """Абстрактный класс - метод для создания продукта из словаря данных."""
        ...
    