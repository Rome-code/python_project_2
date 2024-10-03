import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from tests.conftest import (card_number_generator_exp_result_0_5, card_number_generator_exp_result_1_5,
                            card_number_generator_exp_result_2_2050, description_res, exp_with_result_rub,
                            exp_with_result_usd, result_rub, result_usd, transactions)

"""Параметризация для filter_by_currency"""


@pytest.mark.parametrize(
    "value, currency, expected",
    [
        ([], "USD", [[]]),
        ([], "RUB", [[]]),
        (transactions, "USD", result_usd),
        (transactions, "RUB", result_rub),
        (result_rub, "USD", []),
        (result_usd, "RUB", []),
    ],
)
def test_filter_by_currency_various_input_data(value, currency, expected):
    result = list(filter_by_currency(value, currency))
    assert result == expected


"""Параметризация для transaction_descriptions"""


@pytest.mark.parametrize(
    "value, expected",
    [
        (transactions, description_res),
        (result_usd, exp_with_result_usd),
        (result_rub, exp_with_result_rub),
        ([], [[]]),
    ],
)
def test_transaction_descriptions(value, expected):
    result = list(transaction_descriptions(value))
    assert result == expected


"""Параметризация для card_number_generator"""


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, card_number_generator_exp_result_1_5),
        (2000000000000000, 2000000000000010, card_number_generator_exp_result_2_2050),
        (0, 5, card_number_generator_exp_result_0_5),
        (0, 0, []),
        (1, 0, []),
        (8, 5, []),
        (5,5, [])
    ]
)
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert result == expected
