"""
Repository — слой доступа к данным.

Экспортирует все репозитории для удобного импорта:
    from repository import BaseRepository
"""

from .base_repository import BaseRepository

# Добавляйте новые репозитории здесь:
# from .example.example_repository import ExampleRepository

__all__ = [
    "BaseRepository",
    # "ExampleRepository",
]
