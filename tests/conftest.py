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
