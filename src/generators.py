from tests.conftest import transactions, description_res, result_usd, result_rub

def filter_by_currency(transaction_list, currency):
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            if transaction.get("operationAmount", [{}]).get("currency", [{}]).get("code", [{}]) == currency:
                yield transaction
    else:
        yield []


usd_transactions = filter_by_currency([], "USD")
# try:
#     for i in range(len(transactions)):
#         print(next(usd_transactions))
#
# except StopIteration:
#     pass


def transaction_descriptions(transaction_list):
    if len(transaction_list) > 0:
        for transaction in transaction_list:
            yield transaction.get("description")
    else:
        yield []


# descriptions = transaction_descriptions(result_rub)
# for _ in range(len(result_rub)):
#     print(next(descriptions))


def card_number_generator(start, stop):
    if start == 0 and stop > 0:
        start += 1
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            if start < 1000000000000000:
                card_number = '0' + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number


for card_number in card_number_generator(0, 5):
    print(card_number)
