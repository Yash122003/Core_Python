import datetime

currentdate = datetime.datetime.now()
dob = int(input("enter your date of birth"))
currentage = dob - currentdate
print("your age is", currentage)
