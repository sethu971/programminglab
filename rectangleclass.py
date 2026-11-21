class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    def area(self):
        return self.__length * self.__breadth

    # Overloading < operator
    def __lt__(self, other):
        return self.area() < other.area()


# Creating objects
r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

# Comparing areas
if r1 < r2:
    print("Rectangle 1 has smaller area")
else:
    print("Rectangle 2 has smaller or equal area")