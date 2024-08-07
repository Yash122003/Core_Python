class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):


e = Employee()
e.empCount
print("Name :", self.name, "Salary :", self.salary)

#
#
# class calculation:
#
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#
# C = calculation()
# C.add(10, 20)
# print(C.sum())

#
# class Calculation:
#
#     def number(self, a, b):
#         self.a = a
#         self.b = b
#
#     def sum(self):
#         return self.a + self.b
#
#     def multiply(self):
#         return self.a * self.b
#
#     def divison(self):
#         return self.a / self.b
#
#     def substract(self):
#         return self.a - self.b
#
#
# N = Calculation()
# N.number(40, 50)
# print("\n", N.sum(), "\n", N.divison(), "\n", N.substract(), "\n", N.multiply())
