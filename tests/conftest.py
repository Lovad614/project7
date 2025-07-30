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


# Фикстура транзакций
@pytest.fixture
def transac():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 123456789,
            "state": "EXECUTED",
            "date": "2023-01-01T00:00:00.000000",
            "operationAmount": {"amount": "100.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 1234567890123456",
            "to": "MasterCard 9876543210987654",
        },
        {
            "id": 987654321,
            "state": "EXECUTED",
            "date": "2023-01-02T00:00:00.000000",
            "description": "Перевод без указания валюты",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]


# проверяющие, что функция корректно фильтрует транзакции по заданной валюте.
@pytest.fixture
def rub_transaction():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture
def usd_transaction():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


# не корректорная транзакция
@pytest.fixture
def invalid_transaction():
    return {"operationAmount": {"amount": "invalid", "currency": {"code": "USD"}}}
