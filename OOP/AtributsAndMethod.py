# class shape:
#     Name = "Circle"
#
#
# s = shape()
# print(s.Name)


class shape:
    name = "Circle"
    def change_name(self,new_name):
        self.name= new_name


s = shape()
s.change_name("Rectangle")
print(s.name)
