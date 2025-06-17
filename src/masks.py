def get_mask_card_number(card_number: int) -> str:
    str_card_number = str(card_number)
    if len(str_card_number) != 16:
        raise ValueError("Номер карты должен содержать 16 симболов")
    str_mask_card = f"{str_card_number[:4]} {str_card_number[4:6]}** **** {str_card_number[-4:]}"
    return str_mask_card


def get_mask_account(account_number: int) -> str:
    str_account_number = str(account_number)
    str_mask_account = f"**{str_account_number[-4:]}"
    return str_mask_account
