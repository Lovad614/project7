from src.masks import get_mask_account, get_mask_card_number
'''импортировал из маск функции'''


def mask_account_card(account_card: str) -> str :

    """скрываем счет и номер карты с помощью функций"""

    if "счет" in account_card:
        number_card = account_card[-10:]
        masked_card = get_mask_account(number_card)
        return f"Счет {masked_card}"
    else:
        name_card = account_card[-16:]
        masked = get_mask_card_number(name_card)
        bank_name = account_card[:-16]
        return f"{bank_name} {masked}"


def get_date(data_number: str) -> str:
    """функция получает информацию о дате и переделает ее по нашей"""
    correct = data_number[8:10] + "." + data_number[5:7] + "." + data_number[:4]
    return correct


if __name__ == '__main__':

    print(mask_account_card('Visa Platinum 7000792289606361'))
    print(mask_account_card('Cчет 73654108430135874305'))
    print(get_date("1981-11-17T00:00:01.136347"))
