from src.product_category import Category, Product


def test_product_init(info_product: Product) -> None:
    """Проверка инициализации Product."""
    assert info_product.name == "Samsung Galaxy S23 Ultra"
    assert info_product.description == "256GB, Серый цвет, 200MP камера"
    assert info_product.price == 180000.0
    assert info_product.quantity == 5


def test_category_init(info_category: Category) -> None:
    """Проверка инициализации Category."""
    assert info_category.name == "Смартфоны"
    assert info_category.description == (
        "Смартфоны, как средство не только коммуникации, но и получения " "дополнительных функций для удобства жизни"
    )
    assert len(info_category.products) == 3


def test_count(info_category: Category) -> None:
    """Проверка подсчета количества продуктов и подсчет количества категорий."""
    assert info_category.product_count == 6         # для теста проверка через терминал дает такой результат
    assert info_category.category_count == 2        # без файла json результат 3 и 1
