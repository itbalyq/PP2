import datetime

x = datetime.datetime.now()

#1
five_days_ago = x - datetime.timedelta(days=5)
print(five_days_ago)

#2
yesterday = x - datetime.timedelta(days=1)
tomorrow = x + datetime.timedelta(days=1)
print(yesterday)
print(x)
print(tomorrow)

#3
rounded_datetime = x.replace(microsecond=0)
print(rounded_datetime)

#4
date1 = datetime.datetime(2022, 1, 1, 12, 0, 0)
date2 = datetime.datetime(2022, 1, 2, 12, 0, 0)
difference_seconds = (date2 - date1).total_seconds()
print(difference_seconds)