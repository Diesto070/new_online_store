import pytest

from src.product_category import Category, Product


@pytest.fixture
def info_product() -> Product:
    """Пример продукта для тестов."""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


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
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения" " дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )


@pytest.fixture
def product_with_cost1() -> Product:
    """пример продукта для расчета стоимости"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_with_cost2() -> Product:
    """пример продукта для расчета стоимости"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
