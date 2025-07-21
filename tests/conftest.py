from typing import Any

import pytest


# Фикстура для тестовых данных карт
@pytest.fixture
def card_number() -> dict[str, str]:
    return {"valid": "1234567812345678", "invalid_length": "12345678", "valid_with_spaces": "1234 5678 1234 5678"}


# Фикстура для тестовых данных счетов
@pytest.fixture
def account_number() -> dict[str, str]:
    return {
        "valid": "12345678901234567890",
        "invalid_length": "12345678",
        "invalid_characters": "1234567890abcdef1234",
    }


# Фикстура для тестовых данных транзакций
@pytest.fixture
def transactions_data() -> list[dict[str, Any]]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-10-01"},
        {"id": 2, "state": "PENDING", "date": "2023-09-30"},
        {"id": 3, "state": "EXECUTED", "date": "2023-10-02"},
        {"id": 4, "state": "CANCELLED", "date": "2023-10-03"},
        {"id": 5, "state": "PENDING", "date": "2023-10-01"},
    ]


# Фикстура для строк с датами
@pytest.fixture
def date_number() -> dict[str, str]:
    return {"valid": "2023-10-05T14:48:00.000", "invalid": "05-10-2023"}
