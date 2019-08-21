#challenge 1
class apple:
    def __init__(self, size, color, rot, weight):
        self.size = size
        self.color = color
        self.rot = rot
        self.weight = weight
        
        
 #challenge 2
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())


#challenge 3
class Triangle():
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def triangle_area(self):
        return self.l * self.w / 2
a_triangle = Triangle(20, 30)
print(a_triangle.triangle_area())

#challenge4
class Hexagon():
    def __init__(self, a):
        self.a = a

    def Hex_perimeter(self):
        return self.a * 6
a_hexagon = Hexagon(4)
print(a_hexagon.Hex_perimeter())
