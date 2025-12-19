from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Инициализация продукта.
    name: Название продукта
    description: Описание продукта
    price: Цена (с копейками)
    quantity: Количество в наличии (шт.)
    """

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта."""
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        super().__init__(name, description, quantity)
        self.__price = price
        print(repr(self))

    def __str__(self) -> str:
        """Строковое отображение продукта"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> float:
        """Возвращает суммарную стоимость продуктов (цена × количество)."""
        if type(other) is Product:
            price_sum = self.price * self.quantity + other.price * other.quantity
            return price_sum
        raise TypeError

    @property
    def price(self) -> float:
        """Геттер для цены продукта."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для цены продукта с проверкой."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_date: dict) -> "Product":
        """Класс - метод для создания продукта из словаря данных.
        Args:
        product_data: Словарь с параметрами продукта:
        {
            'name': str,
            'description': str,
            'price': float,
            'quantity': int,
            'color': str
        }
        Returns:
            Созданный объект класса Product"""
        return cls(
            name=product_date["name"],
            description=product_date["description"],
            price=product_date["price"],
            quantity=product_date["quantity"],
        )


class Category:
    """Инициализация категории.
    name: Название категории
    description: Описание категории
    products: Список продуктов (объектов класса Product)
    """

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self) -> str:
        """Строковое отображение категории, количество продуктов считается из общего числа всех продуктов на складе."""
        quantity_sum = 0
        for product in self.__products:
            quantity_sum += product.quantity
        return f"{self.name}, количество продуктов: {quantity_sum} шт.\n"

    @property
    def products_list(self) -> list[Product]:
        """Возвращает список продуктов категории."""
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех продуктов."""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
        