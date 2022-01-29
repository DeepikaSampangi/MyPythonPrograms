import datetime as dt

now = dt.datetime.now()
now
print(now.year)
print(now.date())
print(now.day)

date_of_birth = dt.datetime(year=1996, month=9, day=26)
print(date_of_birth)
