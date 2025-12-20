import pytest

from src.product_category import Category, Product
from src.smartphone_product import Smartphone


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
    # assert len(info_category.products) == 3


def test_count(info_category: Category) -> None:
    """Проверка подсчета количества продуктов и подсчет количества категорий."""
    assert info_category.product_count == 6  # для теста проверка через терминал дает такой результат
    assert info_category.category_count == 2  # без файла json результат 3 и 1


def test_price(info_product: Product) -> None:
    """Тест на корректное изменение цены"""
    info_product.price = 800
    assert info_product.price == 800
    info_product.price = 12000
    assert info_product.price == 12000


def test_price_zero(info_product: Product, capsys: pytest.CaptureFixture[str]) -> None:
    """Тест на недопустимые значения цены"""
    info_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    info_product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_new_product() -> None:
    """Тестируем создание продукта из словаря"""
    test_data = {
        "name": "Samsung Galaxy Ultra",
        "description": "1TB, Красный цвет, 200MP камера",
        "price": 15000,
        "quantity": 3,
        "color": "red",
    }
    product = Product.new_product(test_data)

    assert product.name == "Samsung Galaxy Ultra"
    assert product.description == "1TB, Красный цвет, 200MP камера"
    assert product.price == 15000
    assert product.quantity == 3
    assert product.color == "red"


def test_product_list(info_category: Category) -> None:
    """Тестирует количество продуктов в категории"""
    assert len(info_category.products_list) == 3

    # Проверяем, что это список
    assert isinstance(info_category.products_list, list)


def test_products_str() -> None:
    """Возвращает строковое представление продуктов."""
    product1 = Product("Samsung Galaxy S23 Ultra", "Смартфон", 150000, 4, "red")
    product2 = Product("Ноутбук", "Игровой", 50000, 3, "green")

    category = Category("Электроника", "Техника", [product1, product2])
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 150000 руб. Остаток: 4 шт.\nНоутбук, 50000 руб. Остаток: 3 шт.\n"
    )


def test_add_product() -> None:
    """Тестирует корректность добавления продукта в категорию."""
    category = Category("Телефоны", "Смартфоны", [])
    product = Product("iPhone", "Смартфон", 50000, 10, "red")
    assert len(category.products_list) == 0
    category.add_product(product)
    assert len(category.products_list) == 1

def test_product_str(info_product: Product) -> None:
    """Тестирует строковое представление продукта."""
    assert str(info_product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(info_category_: Category) -> None:
    """Тестирует строковое представление категории."""
    assert str(info_category_.products) == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_category_str_with_single_product() -> None:
    """Тестирует строковое представление категории с одним продуктом."""
    product = Product("Мышь", "Компьютерная", 1500, 10, "red")
    category = Category("Аксессуары", "Для ПК", [product])
    assert str(category) == "Аксессуары, количество продуктов: 10 шт.\n"


def test_category_str_with_no_product() -> None:
    """Тестирует строковое представление категории с пустым продуктом."""
    category = Category("Книги", "Литература", [])
    assert str(category) == "Книги, количество продуктов: 0 шт.\n"


def test_product_add(product_with_cost1: Product, product_with_cost2: Product) -> None:
    """Тестирует корректность сложения общей стоимости двух продуктов."""
    assert product_with_cost1 + product_with_cost2 == 2580000


def test_product_add_error(product_with_cost1: Product) -> None:
    """Тестирует обработку ошибки при попытке сложения Product с несовместимым типом.
    Проверяет, что при попытке сложить объект Product с объектом другого типа
    (в данном случае с integer) возникает исключение TypeError.

    Args:
        product_with_cost1: Фикстура с тестовым объектом Product
    """
    with pytest.raises(TypeError):
        result = product_with_cost1 + 1


def test_category_product_add_error() -> None:
    """Тестирует обработку ошибки при попытке добавления не-продукта в категорию.

    Проверяет, что при попытке добавить в категорию объект, не являющийся
    экземпляром Product или его подклассов, возникает исключение TypeError.
    """
    category = Category("Электроника", "орыапры", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")


def test_category_product_add(info_category_: Category, product_smartphone1: Smartphone) -> None:
    """Тестирует добавление смартфона в категорию.
    Проверяет корректность добавления объекта Smartphone в список продуктов категории
    и проверяет, что последний добавленный продукт имеет ожидаемое имя.

    Args:
        info_category_: Фикстура с тестовой категорией, содержащей продукты
        product_smartphone1: Фикстура с тестовым объектом смартфона
    """
    info_category_.add_product(product_smartphone1)
    assert info_category_.products_list[-1].name == "Samsung Galaxy S23"
    
