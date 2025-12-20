import pytest

from src.lawngrass_product import LawnGrass


def test_lawngrass_product_init(product_lawngrass1: LawnGrass) -> None:
    """Тестирует корректность инициализации объекта LawnGrass.
    Проверяет, что все атрибуты объекта газонной травы устанавливаются правильно
    и соответствуют ожидаемым значениям, включая наследуемые от Product и специфичные для LawnGrass.

    Args:
        product_lawngrass1: Фикстура с тестовым объектом газонной травы
    """
    assert product_lawngrass1.name == "Газонная трава"
    assert product_lawngrass1.description == "Элитная трава для газона"
    assert product_lawngrass1.price == 500.0
    assert product_lawngrass1.quantity == 20
    assert product_lawngrass1.country == "Россия"
    assert product_lawngrass1.germination_period == "7 дней"
    assert product_lawngrass1.color == "Зеленый"


def test_lawngrass_product_add(product_lawngrass1: LawnGrass, product_lawngrass2: LawnGrass) -> None:
    """Тестирует корректность сложения двух объектов LawnGrass.
    Проверяет, что оператор + правильно вычисляет суммарную стоимость
    товаров на основе цены и количества для объектов газонной травы.

    Args:
        product_lawngrass1: Фикстура с первым тестовым объектом газонной травы
        product_lawngrass2: Фикстура со вторым тестовым объектом газонной травы
    """
    assert product_lawngrass1 + product_lawngrass2 == 16750.0


def test_lawngrass_product_add_error(product_lawngrass1: LawnGrass) -> None:
    """Тестирует обработку ошибки при попытке сложения LawnGrass с несовместимым типом.
    Проверяет, что при попытке сложить объект LawnGrass с объектом другого типа
    (в данном случае с integer) возникает исключение TypeError.

    Args:
        product_lawngrass1: Фикстура с тестовым объектом газонной травы
    """
    with pytest.raises(TypeError):
        product_lawngrass1 + 1
        
