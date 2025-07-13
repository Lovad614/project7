import pytest
from src.masks import get_mask_card_number, get_mask_account

# Фикстура для тестовых данных карт
@pytest.fixture
def card_number():
    return {
        "valid": "1234567812345678",
        "invalid_length": "12345678",
        "valid_with_spaces": "1234 5678 1234 5678"
    }

# Фикстура для тестовых данных счетов
@pytest.fixture
def account_number():
    return {
        "valid": "12345678901234567890",
        "invalid_length": "12345678",
        "invalid_characters": "1234567890abcdef1234"
    }

def test_get_mask_card_number_valid(card_number):
    expected_result = "1234 56** **** 5678"
    assert get_mask_card_number(card_number["valid"]) == expected_result


def test_get_mask_card_number_invalid_length(card_number):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = str(card_number["invalid_length"])
    assert get_mask_card_number(card_number["invalid_length"]) == expected_result


def test_get_mask_account_valid(account_number):
    expected_result = "**7890"
    assert get_mask_account(account_number["valid"]) == expected_result


def test_get_mask_account_invalid_length(account_number):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = account_number["invalid_length"]
    assert get_mask_account(account_number["invalid_length"]) == expected_result

def test_get_mask_account_invalid_characters(account_number):
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    expected_result = account_number["invalid_characters"]
    assert get_mask_account(account_number["invalid_characters"]) == expected_result