import datetime

today=datetime.date.today()
print(today.year)
print(today.weekday())

tDelta=datetime.timedelta(days=8)

print(today+tDelta)
