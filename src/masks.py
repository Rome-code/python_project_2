def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    if len(card_number) == 16 and card_number.isdigit() == True:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "некорректный ввод"

def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    if len(account_number) == 20 and account_number.isdigit() == True:
        return f"**{account_number[-4:]}"
    return "некорректный ввод"