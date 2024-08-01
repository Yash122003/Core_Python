import datetime

a = datetime.datetime.now()
# print(a)
# b = datetime.datetime(day=30, month=7, year=2024)
# print(b)
# print(a.day, a.month, a.year)


# import datetime
#
# a = datetime.datetime.now()
# print(a.day,a.month,a.year)
print(a.strftime("%V"))
