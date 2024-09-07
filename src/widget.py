from masks import get_mask_account, get_mask_card_number

account_type_card_num = input()


def mask_account_card(account_type_card_num: str) -> str:
    account_type_card_num_list = account_type_card_num.split(" ")
    if len(account_type_card_num_list[-1]) < 20:
        mask_card_number = get_mask_card_number(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_card_number

        return " ".join(account_type_card_num_list)
    else:
        mask_account = get_mask_account(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_account
        return " ".join(account_type_card_num_list)

def get_date(date_and_time: str) -> str:
    pass
print(mask_account_card(account_type_card_num))