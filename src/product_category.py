class Product:
    """Инициализация продукта.
    name: Название продукта
    description: Описание продукта
    price: Цена (с копейками)
    quantity: Количество в наличии (шт.)
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
            'quantity': int
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

    name: str
    description: str
    products: list[Product]
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self) -> str:
        """Возвращает строковое представление всех продуктов."""
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity}шт.\n"
        return product_str

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1
