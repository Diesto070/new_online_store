import pytest

from src.lawngrass_product import LawnGrass
from src.product_category import Category, Product
from src.smartphone_product import Smartphone


@pytest.fixture
def info_product() -> Product:
    """Пример продукта для тестов."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "red")


@pytest.fixture
def info_category(
    product1=None,
    product2=None,
    product3=None,
) -> Category:
    """пример категории с одним продуктом."""
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения" " дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def info_category_() -> Category:
    """пример категории с продуктами."""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "red")
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "green")
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, "black")

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения" " дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )


@pytest.fixture
def product_with_cost1() -> Product:
    """пример продукта для расчета стоимости"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "red")


@pytest.fixture
def product_with_cost2() -> Product:
    """пример продукта для расчета стоимости"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8, "green")


@pytest.fixture
def product_smartphone1() -> Smartphone:
    """Пример продукта для создания тестового объекта смартфона Samsung Galaxy S23 Ultra.
    Returns:
        Smartphone: Объект смартфона с предустановленными характеристиками
    """
    return Smartphone(
        "Samsung Galaxy S23", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def product_smartphone2() -> Smartphone:
    """Пример продукта для создания тестового объекта смартфона iPhone 15.
    Returns:
        Smartphone: Объект смартфона с предустановленными характеристиками
    """
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def product_lawngrass1() -> LawnGrass:
    """Пример продукта для создания тестового объекта газонной травы (элитный сорт).
    Returns:
        LawnGrass: Объект газонной травы с предустановленными характеристиками
    """
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def product_lawngrass2() -> LawnGrass:
    """Пример продукта для создания тестового объекта газонной травы (выносливый сорт).
    Returns:
        LawnGrass: Объект газонной травы с предустановленными характеристиками
    """
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
