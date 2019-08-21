class Shape():#challenge 3
    def what_am_i(self):
        print("I am a shape")

#Challenge 1
class Rectangle(Shape):#inherit shap challenge 3 
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
class Square(Shape):#inherit shap challenge 3 
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4
    def change_size(self, new_size):
         self.s1 = new_size #challenge 2       
    
a_rectangle = Rectangle(25, 50)#challenge 1
a_square = Square(20)#challenge 1

print(a_rectangle.calculate_perimeter())#challenge 1
print(a_square.calculate_perimeter())#challenge 1

a_square = Square(2001)#challenge 2
print(a_square.s1)
a_square.change_size(-200)#challenge 2
print(a_square.s1)

a_rectangle.what_am_i()#challenge 3
a_square.what_am_i()#challenge 3


#challenge 4
class Horse():
    def __init__(self, name):
        self.name = name
        
class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse
bently_the_horse = Horse("Bently")
the_rider = Rider("Reggie", bently_the_horse)
print(the_rider.horse.name)
print(the_rider.name)


        





    
