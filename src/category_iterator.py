from typing import Iterator

from src.product_category import Category, Product


class CategoryIterator:
    """Итератор для последовательного перебора продуктов в категории.
    Позволяет итерироваться по продуктам категории один за другим."""

    def __init__(self, category_obj: Category) -> None:
        self.category = category_obj
        self.index = 0

    def __iter__(self) -> Iterator[Product]:
        """Возвращает сам итератор для использования в цикле for."""
        self.index = 0
        return self

    def __next__(self) -> Product:
        """Возвращает следующий продукт в категории."""
        if self.index < len(self.category.products_list):
            product = self.category.products_list[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    iterator = CategoryIterator(category)

    for product in iterator:
        print(product)
