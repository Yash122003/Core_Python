# class Parent:
#     def show(self):
#         print("Parent method called")
#
#
# class Child(Parent):
#     def display(self):
#         print("Child method called")
#
#
# obj = Child()
#
# obj.show()
# obj.display()





# Inheritence of shapes , rectangle , circle , tirangle
class Shape:

    def __init__(self, Color):
        self.Color = Color

    def getcolor(self):
        return self.Color


class rectangle(Shape):

    def __init__(self, length, width, Color):
        super().__init__(Color)
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


r = rectangle(54, 67, "red")
print("Area of Rectangle=",r.area(),"\nColor of rectangle=", r.getcolor())


class circle(Shape):

    def __init__(self, radius, Color):
        super().__init__(Color)

        self.pi = 22 / 7
        self.radius = radius

    def area(self):
        return self.pi * self.radius ** 2


c = circle(5, "green")
print("Area of Circle=",c.area(),"\nColor of Circle=", c.getcolor())


class triangle(Shape):

    def __init__(self, base, hight, Color):
        super().__init__(Color)
        self.base = base
        self.hight = hight

    def area(self):
        return self.base * self.hight


t = triangle(5, 6, "blue")
print("Areav of Triangle=","\nColor of Triangle=", t.area(), c.getcolor())

