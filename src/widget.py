from src.masks import get_mask_account, get_mask_card_number

"""импортировал из маск функции"""


def mask_account_card(account_card: str) -> str:
    """скрываем счет и номер карты с помощью функций"""

    if "Счет" == account_card[:4]:
        number_card = account_card[-20:]
        masked_card = get_mask_account(int(number_card))
        return f"Счет {masked_card}"
    else:
        name_card = account_card[-16:]
        masked = get_mask_card_number(int(name_card))
        bank_name = account_card[:-16]
        return f"{bank_name}{masked}"


def get_date(data_number: str) -> str:
    """функция получает информацию о дате и переделает"""
    correct = data_number[8:10] + "." + data_number[5:7] + "." + data_number[:4]
    return correct
