from data_generator import initialize_data
import decimal
from operator import itemgetter
import time
from functools import wraps


def timing(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = time.process_time()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = time.process_time() - start
            print(f"Total execution time: {end_*1000 if end_ > 0 else 0} ms")
    return _time_it




def read_transaction(transaction):

    return transaction[0], transaction[1], transaction[2], decimal.Decimal(transaction[3])

@timing
def process_ledger():

    ledger = initialize_data(5, 10)
    ledger = sorted(ledger, key=itemgetter(0))

    for element in ledger:
        print(element)

    customer_dict ={}
    for transaction in ledger:

        date, payer, payee, amount = read_transaction(transaction)

        if payer not in customer_dict:
            customer_transaction_dict = {}
            customer_transaction_dict[date] = -amount
            customer_dict[payer] = customer_transaction_dict
        else:
            customer_transaction_dict = customer_dict[payer]

            if date in customer_transaction_dict:
                date_balance = customer_transaction_dict[date]
                customer_transaction_dict[date] = date_balance-amount
            else:
                customer_transaction_dict[date]=-amount

        if payee not in customer_dict:
            customer_transaction_dict = {}
            customer_transaction_dict[date] = amount
            customer_dict[payee] = customer_transaction_dict
        else:
            customer_transaction_dict = customer_dict[payee]

            if date in customer_transaction_dict:
                date_balance = customer_transaction_dict[date]
                customer_transaction_dict[date] = date_balance+amount
            else:
                customer_transaction_dict[date]=amount

    return customer_dict


# print(process_ledger(ledger))

def get_balance_by_name_date(name, date):

    processed_ledger = process_ledger()

    customer_transaction_dict = processed_ledger[name]

    balance=0
    for key, value in customer_transaction_dict.items():
        balance +=value
        if key == date:
            break


    return balance

print(get_balance_by_name_date('benjamin','2020-06-14'))