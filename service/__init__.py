"""
Service — бизнес-логика приложения.

Экспортирует все сервисы для удобного импорта:
    from service import HealthService
"""

from .health.health_service import HealthService

# Добавляйте новые сервисы здесь:
# from .example.example_service import ExampleService

__all__ = [
    "HealthService",
    # "ExampleService",
]
