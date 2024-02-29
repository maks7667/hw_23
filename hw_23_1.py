import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, other):
        return Circle(self.radius + other)

    def __sub__(self, other):
        return Circle(self.radius - other)

    def __iadd__(self, other):
        self.radius += other
        return self

    def __isub__(self, other):
        self.radius -= other
        return self

    def __repr__(self):
        return f"Circle(radius={self.radius})"

    def circumference(self):
        return 2 * math.pi * self.radius

if __name__ == "__main__":
    circle1 = Circle(5)
    circle2 = Circle(7)
    circle3 = Circle(5)

    print(circle1 == circle2)  
    print(circle1 == circle3)  

    print(circle1 < circle2)   
    print(circle1 <= circle3)  
    print(circle1 > circle2)   
    print(circle2 >= circle3)  

    print(circle1 + 3)         
    print(circle2 - 2)         

    circle1 += 2
    print(circle1)             

    circle2 -= 1
    print(circle2)             

    print(circle1.circumference())  
