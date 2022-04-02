class Shape():
    def what_am_i(self):
        print("Я-Фигура.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

class Square(Shape):
    def __init__(self, sq):
        self.sq = sq

r1=Rectangle(20,30)
s1=Square(20)
s1class Shape():
    def what_am_i(self):
        print("Я-Фигура.")

class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

class Square(Shape):
    def __init__(self, sq):
        self.sq = sq

r1=Rectangle(20,30)
s1=Square(20)
s1.what_am_i()
r1.what_am_i()
