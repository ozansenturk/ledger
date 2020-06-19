from faker import Faker
from random import randrange
import random

seed =2023
fake = Faker()
fake.random.seed(seed)
random.seed(seed)

def get_names(how_many=10):
    names = [fake.first_name().lower() for i in range(0,how_many)]
    return names

def get_dates(how_many=10, how_many_days_before='-10d'):
    dates = [fake.date_between(start_date=how_many_days_before).strftime('%Y-%m-%d') for i in range(0, how_many)]

    return dates
    # return sorted(dates)


dates = get_dates()


def get_amount(how_many=10):
    amount_list = ['{:,.2f}'.format(randrange(5,100,5)) for i in range(0,how_many)]
    return amount_list

def initialize_data(how_many=10, ledger_size=100):

    names = get_names(how_many)
    dates = get_dates(how_many)
    money = get_amount(how_many)

    ledger = []
    for i in range(0,ledger_size):
        date_column = random.choice(dates)
        amount_column = random.choice(money)
        payer_column = random.choice(names)
        payee_column = payer_column

        while(payer_column==payee_column):
            payee_column = random.choice(names)

        ledger.append([date_column,payer_column,payee_column,amount_column])

    return ledger

ledger = initialize_data(5,10)




