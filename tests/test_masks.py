from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тест на срабатывание функции при введении номера карты"""
    assert get_mask_card_number(4276060032300678) == "4276 06** **** 0678"


# def test_get_mask_account_basic():
#     assert get_mask_account(12345678901234567890) == **7890