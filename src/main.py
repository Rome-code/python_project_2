from masks import get_mask_account, get_mask_card_number

"""Импортируем функции маскировки номера счета и аккаунта из файла masks.py
и запрашиваем номер счета и карты"""

card_number_str: str = input("Введите номер карты: ")
account_num: str = input("Введите номер счета: ")

"""Проверяем корректность ввода условием, 
в случае выполнения условия - вывод информации в маске."""

if len(card_number_str) == 16:
    print(get_mask_card_number(card_number_str))
else:
    print("Некорректный ввод номера карты")

if len(account_num) == 20:
    print(get_mask_account(account_num))
else:
    print("Некорректный ввод номера счета")
