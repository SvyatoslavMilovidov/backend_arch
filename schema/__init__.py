"""
Schema — Pydantic схемы для валидации данных.

Экспортирует все схемы для удобного импорта:
    from schema import HealthCheckResponseSchema
"""

from .health.health_schema import HealthCheckResponseSchema

# Добавляйте новые схемы здесь:
# from .example.example_schema import ExampleCreateSchema, ExampleResponseSchema

__all__ = [
    "HealthCheckResponseSchema",
    # "ExampleCreateSchema",
    # "ExampleResponseSchema",
]
