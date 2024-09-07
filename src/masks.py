"""Функция для маскировки номера карты"""


def get_mask_card_number(card_number: str) -> str:
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


"""Функция для маскировки номера счета"""


def get_mask_account(account_number: str) -> str:
    return f"**{account_number[-4:]}"
