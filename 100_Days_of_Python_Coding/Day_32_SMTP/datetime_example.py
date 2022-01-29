import datetime as dt
import os
import random

curr_dir = os.path.dirname(__file__)
now = dt.datetime.now()
now
print(now.year)
print(now.date())
print(now.day)

date_of_birth = dt.datetime(year=1996, month=9, day=26)
print(date_of_birth)

if now.weekday == 0:
    with open(curr_dir + "/quotes.txt") as file:
        quotes = file.readlines()
        print(random.choice(quotes))
