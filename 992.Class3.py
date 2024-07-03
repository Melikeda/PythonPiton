class circle:

    # class object attribute

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # methods
    
    def circumference(self):
        return 2 * self.pi * self.radius
    
    def area(self):
        return  self.pi * (self.radius**2)
    
c1 = circle()
c2 = circle(5)


print(f"c1 circumference = {c1.circumference()} c1 area = {c1.area()}")
print(f"c2 circumference = {c2.circumference()} c2 area = {c2.area()}")

