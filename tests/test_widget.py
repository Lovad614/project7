from src.widget import get_date, mask_account_card


def test_mask_account_card(card_number: dict[str, str], account_number: dict[str, str]) -> None:
    assert mask_account_card(f"Счет {account_number['valid']}") == "Счет **7890"
    assert mask_account_card(f"Карта VISA {card_number['valid']}") == "Карта VISA 1234 56** **** 5678"


def test_get_date(date_number: dict[str, str]) -> None:
    assert get_date(date_number["valid"]) == "05.10.2023"
