from typing import Any


class PrintMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация миксина.
        Args:
            *args: Произвольные позиционные аргументы
            **kwargs: Произвольные ключевые аргументы
        """
        super().__init__(*args, **kwargs)

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта."""
        return (
            f"{self.__class__.__name__}("
            f"{self.name}, "
            f"{self.description}, "
            f"{getattr(self, 'price', 'N/A')}, "
            f"{self.quantity})"
        )
