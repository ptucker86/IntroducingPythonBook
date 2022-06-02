# pg 135

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    # name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.name

print(fowl._Duck__name)