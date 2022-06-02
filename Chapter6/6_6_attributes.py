# pg 133

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    # name = property(get_name, set_name)

fowl = Duck('Howard')
# print(fowl.name)

fowl.name = 'Daffy'
# print(fowl.name)

# pg 135
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self, diameter):
        self.diameter = diameter
        return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter(c.radius))

c.radius = 7
print(c.diameter)

c.diameter = 20
print(c.radius)
print(c.diameter)