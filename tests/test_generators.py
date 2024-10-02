from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from tests.conftest import (transactions, description_res, result_usd, result_rub, exp_with_result_usd, exp_with_result_rub, card_number_generator_exp_result_1_5, card_number_generator_exp_result_2_2050)
import pytest





'''Параметризация для filter_by_currency'''


@pytest.mark.parametrize(
    "value, currency, expected",[
     ([], 'USD', [[]]),
     ([], 'RUB', [[]]),
     (transactions, 'USD', result_usd),
     (transactions, 'RUB', result_rub),
     (result_rub, 'USD', []),
     (result_usd, 'RUB', [])
    ]
)
def test_filter_by_currency_various_input_data(value, currency, expected):
    result = list(filter_by_currency(value, currency))
    assert result == expected


'''Параметризация для transaction_descriptions'''


@pytest.mark.parametrize(
    "value, expected", [
        (transactions, description_res),
        (result_usd, exp_with_result_usd),
        (result_rub, exp_with_result_rub),
        ([], [[]])
    ]
)
def test_transaction_descriptions(value, expected):
    result = list(transaction_descriptions(value))
    assert result == expected


'''Параметризация для card_number_generator'''

num_1 = 1
num_2 = 5
num_3 = 2000000000000000
num_4 = 2000000000000010


@pytest.mark.parametrize(
    "start, stop, expected", [
        (num_1, num_2, card_number_generator_exp_result_1_5),
        (num_3, num_4, card_number_generator_exp_result_2_2050)
    ]
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected