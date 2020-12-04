import random as rnd
import csv

count = 50000
file_name = 'numbers.csv'

numbers = []
with open(file_name, 'w', newline='') as csvfile:
    wr = csv.writer(csvfile)

    for i in range(0, count):
        wr.writerow([rnd.random()])
