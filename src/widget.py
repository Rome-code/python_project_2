from masks import get_mask_account, get_mask_card_number

"""Ввод номера карты или номера счета"""
account_type_card_num = input()


def mask_account_card(account_type_card_num: str) -> str:
    """Функция, для выводв номера карты или счета с текстом"""
    account_type_card_num_list = account_type_card_num.split(" ")
    if len(account_type_card_num_list[-1]) < 20:
        mask_card_number = get_mask_card_number(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_card_number
    else:
        mask_account = get_mask_account(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_account
    return " ".join(account_type_card_num_list)


"""Ввод строки с датой и временем"""
date_and_time = input()


def get_date(date_and_time: str) -> str:
    """Функция, реобразующая date_and_time в ДД.ММ.ГГГГ"""
    if len(date_and_time) == 26 and date_and_time[4] == "-" and date_and_time[7] == "-" and date_and_time[-7] == ".":
        nec_form_date = f"{date_and_time[8:10]}.{date_and_time[5:7]}.{date_and_time[0:4]}"
    return nec_form_date


"""Вызов и возвращение результатов функций"""
print(mask_account_card(account_type_card_num))
print(get_date(date_and_time))
