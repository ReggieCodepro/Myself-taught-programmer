#challenge 1
class Shape():
    def what_am_i(self):
        print("I am a shape.")

class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calulate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")

    #challenge 2
    def __repr__self(self):
        return "{} by {} by {} by {}" .format(self.s1, self.s1, self.s1, self.s1) 

a_square = Square(29)
print(a_square)

#challenge 3
def compare(obj1, obj2):
    return obj1 is obj2
print(compare("a", "b"))
print(compare(1, 1))



