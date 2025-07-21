import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number_valid(card_number: dict[str, str]) -> None:
    expected_result = "1234 56** **** 5678"
    assert get_mask_card_number(int(card_number["valid"])) == expected_result


def test_get_mask_card_number_invalid_length(card_number: dict[str, str]) -> None:
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    with pytest.raises(ValueError):
        get_mask_card_number(int(card_number["invalid_length"]))


def test_get_mask_account_valid(account_number: dict[str, str]) -> None:
    expected_result = "**7890"
    assert get_mask_account(int(account_number["valid"])) == expected_result


def test_get_mask_account_invalid_length(account_number: dict[str, str]) -> None:
    # Ожидается, что функция вернет исходное значение и выведет сообщение об ошибке
    with pytest.raises(ValueError):
        get_mask_account(int(account_number["invalid_length"]))
