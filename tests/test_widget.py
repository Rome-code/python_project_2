import pytest
from src.widget import mask_account_card, get_date
from tests.conftest import date_and_time

'''Тесты для mask_account_card'''

@pytest.mark.parametrize(
    "value, expected", [
        ("Visa Platinum 7000792289606361", 'Visa Platinum 7000 79** **** 6361'),
        ('Счет 73654108430135874305', 'Счет **4305')
        ]
    )
def test_mask_account_card_basic(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected

# @pytest.mark.parametrize(
#     "value, expected", [
#         (),
#         ()
#         ]
#     )
# def test_mask_account_card_various_input_data(value: list, expected: list) -> None:
#     assert mask_account_card(value) == expected


'''Тесты для get_date'''
def test_get_date_basic():
    assert get_date(date_and_time) == '14.10.2018'