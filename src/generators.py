from tests.conftest import transactions


def filter_by_currency(transaction_list, currency):
    for transaction in transaction_list:
        if transaction.get("operationAmount", [{}]).get("currency", [{}]).get("code", [{}]) == currency:
            yield transaction


usd_transactions = filter_by_currency(transactions, "USD")
try:
    for i in range(len(transactions)):
        print(next(usd_transactions))

except StopIteration:
    pass


def transaction_descriptions(transaction_list):
    for transaction in transaction_list:
        yield transaction.get("description")


descriptions = transaction_descriptions(transactions)
for _ in range(len(transactions)):
    print(next(descriptions))


def card_number_generator(start, stop):
    pass


