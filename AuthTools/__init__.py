"""Shared auth library"""
__version__ = "0.1.0"

# Экспортируем основные функции (опционально)
from .models import HeaderUser
from .Permissions import dependencies

__all__ = [
    "HeaderUser",
    "dependencies",
]