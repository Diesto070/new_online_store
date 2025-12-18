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
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


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
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
