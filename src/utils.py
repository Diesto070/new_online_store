import json
from typing import Any, List

from src.product_category import Category, Product


def read_json(path: str) -> List[Any]:
    """Загружает данные из JSON"""
    with open(path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_from_json(data: List[Any]) -> List[Category]:
    categories = []
    for category_data in data:
        products = []
        for product_data in category_data["products"]:
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"]
            )
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)
    return categories


if __name__ == '__main__':
    raw_data = read_json("../data/products.json")
    create_objects_from_json(raw_data)
    print(Category.category_count)
    print(Category.product_count)
    