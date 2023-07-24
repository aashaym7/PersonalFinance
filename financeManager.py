import csv
import gspread
# from decimal import Decimal

MONTH = 'July'

file = f"Amex_{MONTH}.csv"

transactions = []

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    headers = next(csv_file) 
    for row in csv_reader:
        date = row[0]
        name = row[1]
        # amount = Decimal(row[2])
        # amountInt = row[2].replace(" ", "")
        # print(amountInt)
        # amount = float(amountInt)
        amount = float(row[2])
        category = 'other'
        transaction = ((date, name, amount, category))
sa = gspread.service_account()
sh = sa.open("Personal Finances")