import pytest

from src.smartphone_product import Smartphone


def test_smartphone_product_init(product_smartphone1: Smartphone) -> None:
    """Проверка инициализации Smartphone.
    Проверяет, что все атрибуты объекта устанавливаются правильно
    и соответствуют ожидаемым значениям."""
    assert product_smartphone1.name == "Samsung Galaxy S23"
    assert product_smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert product_smartphone1.price == 180000.0
    assert product_smartphone1.quantity == 5
    assert product_smartphone1.efficiency == 95.5
    assert product_smartphone1.model == "S23 Ultra"
    assert product_smartphone1.memory == 256
    assert product_smartphone1.color == "Серый"


def test_smartphone_product_add(product_smartphone1: Smartphone, product_smartphone2: Smartphone) -> None:
    """Тестирует корректность сложения двух объектов Smartphone.
    Проверяет, что оператор + правильно вычисляет суммарную стоимость
    товаров на основе цены и количества.

    Args:
        product_smartphone1: Фикстура с первым тестовым объектом смартфона
        product_smartphone2: Фикстура со вторым тестовым объектом смартфона
    """
    assert product_smartphone1 + product_smartphone2 == 2580000


def test_smartphone_product_add_error(product_smartphone1: Smartphone) -> None:
    """Тестирует обработку ошибки при попытке сложения с несовместимым типом.
    Проверяет, что при попытке сложить Smartphone с объектом другого типа
    возникает исключение TypeError.

    Args:
        product_smartphone1: Фикстура с тестовым объектом смартфона
    """
    with pytest.raises(TypeError):
        product_smartphone1 + 1
