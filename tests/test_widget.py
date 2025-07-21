from src.widget import get_date, mask_account_card


def test_mask_account_card(card_number: dict[str, str], account_number: dict[str, str]) -> None:
    assert mask_account_card(f"Счет {card_number['valid']}") == "Счет  1234 56** **** 5678"
    assert mask_account_card(f"Карта VISA {account_number['valid']}") == "Карта VISA 1234 5678 90** **** 7890"


def test_get_date(date_number: dict[str, str]) -> None:
    assert get_date(date_number["valid"]) == "05.10.2023"
