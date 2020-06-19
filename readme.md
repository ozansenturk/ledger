## PROJECT STRUCTURE
there are two modules: data_generator and transaction

date generator is composed of Faker and Random librarires to form the ledger which
is in the format of ['2020-06-09', 'mary', 'debra', '95.00'] .You can change the seed
to work on different data.

initialize_data function takes 'how many customers' and 'ledger size' as parameter
Each transaction has one date, payer, payee, and amount however a payer cannot be a
payee in the same transaction.

transaction has two sections. Firstly, it creates dictionary of dictionaries, outer
dictionary keeps the customers whilst the inner one the transactions. Next, the
dictionary of dictionaries is the 'processed ledger' which means that it is ready
to calculate the balance for the given date.

## HOW TO RUN
pyhton3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pyhon3 transaction.py

Feel free to ask more information. 
ozan.senturk@gmail.com
www.analyticai.co.uk



  

