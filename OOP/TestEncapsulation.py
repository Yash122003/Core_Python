# import datetime
#
#
# class Person:
#     def __init__(self, name, dob, city):
#         self.name = name
#         self.dob = dob
#         self.city = city
#
#     def getname(self):
#         return self.name
#
#     def getdob(self):
#         D = datetime.datetime.now()
#         Y = D.year
#         return Y - self.dob
#
#     def getcity(self):
#         return self.city
#
#
# P = Person("Yash", 2003, "Barwani")
# print("Name=", P.getname(), "Age=", P.getdob(), "City=", P.getcity())
#
#

class Automobile:
    def __init__(self, Colour, Car, Speed):
        self.Colour = Colour
        self.Car = Car
        self.Speed = Speed

    def getColour(self):
        return self.Colour

    def getCar(self):
        return self.Car

    def getSpeed(self):
        return self.Speed

    def Gear(self):
        if (self.Speed < 1):
            return 1
        if (20 < self.Speed <= 40):
            return 2
        if (40 < self.Speed <= 60):
            return 3
        if (60 < self.Speed <= 80):
            return 4
        if (self.Speed > 80):
            return 5


C = Automobile("Black", "Bmw", 55)
print("Colour=", C.getColour())
print("Car=", C.getCar())
print("Speed=", C.getSpeed())
print(C.Gear())
