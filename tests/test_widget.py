import pytest
from src.widget import mask_account_card, get_date

# Фикстура для номеров карт
@pytest.fixture
def card_numbers():
    return {
        "valid": "1234567812345678",
        "short": "1234",
        "long": "12345678901234567890"
    }

# Фикстура для номеров счетов
@pytest.fixture
def account_numbers():
    return {
        "valid": "12345678901234567890",
        "short": "1234",
        "with_letters": "1234abc7890123456789"
    }

# Фикстура для строк с датами
@pytest.fixture
def date_strings():
    return {
        "valid": "2023-10-05T14:48:00.000",
        "invalid": "05-10-2023"
    }
def test_mask_account_card(number_card, account_card):
    assert mask_account_card(f"Счет {number_card['valid']}") == "Счет ****************7890"
    assert mask_account_card(f"Карта VISA {account_card['valid']}") == "Карта VISA 1234********5678"

def test_get_date(date_number):
    assert get_date(date_number["valid"]) == "05.10.2023"
    with pytest.raises(ValueError):
        get_date(date_number["invalid"])