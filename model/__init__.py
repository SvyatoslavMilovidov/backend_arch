"""
Model — ORM модели приложения.

Экспортирует все модели для удобного импорта:
    from model import Base, ExampleModel
"""

from .base_model import Base, BaseModel
from .enums import ExampleStatusEnum

# Добавляйте новые модели здесь:
# from .example.example_model import ExampleModel

__all__ = [
    "Base",
    "BaseModel",
    "ExampleStatusEnum",
    # "ExampleModel",
]
