# pg 128
from pydoc import doc


class Car():
    def exclaim(self):
        print("I'm a car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Similar to a Car!")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


# pg 130
class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"

person = Person('Fudd')
doctor = MDPerson('Fudd2')
lawyer = JDPerson('Fudd3')

print(person.name)
print(doctor.name)
print(lawyer.name)
