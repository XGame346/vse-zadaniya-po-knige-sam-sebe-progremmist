class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {} """.format(self.width, self.len))

    def calculate_perimetr(self):
        return self.width*2+self.len*2

class Square(Rectangle):
    pass

r1=Rectangle(20,30)
s1=Square(20,20)
print("class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} на {} """.format(self.width, self.len))

    def calculate_perimetr(self):
        return self.width*2+self.len*2

class Square(Rectangle):
    pass

r1=Rectangle(20,30)
s1=Square(20,20)
print("Периметр прямоугольника", r1.calculate_perimetr(), "Периметр квадрата",s1.calculate_perimetr())
