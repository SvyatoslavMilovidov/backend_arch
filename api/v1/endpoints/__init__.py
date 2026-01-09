"""
Endpoints — HTTP роутеры для API v1.
"""

from .health import router as health_router

# Добавляйте новые роутеры здесь:
# from .example import router as example_router

__all__ = [
    "health_router",
    # "example_router",
]
