"""
Define a circle class to create a circle with radius r using the constructor.
Define an Area() method of the class which calculates area of the circle
Define a Perimeter() method of the class which allows you to calculate the perimeter of circle
"""
class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = circle(21)
print(c1.area())
print(c1.perimeter())
