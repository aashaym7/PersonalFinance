import csv
import gspread

MONTH = 'July'

file = f"Amex_{MONTH}.csv"

with open(file, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

sa = gspread.service_account()
sh = sa.open("Personal Finances")