# pg 130

from tkinter.messagebox import YESNO


class Car():
    def exclaim(self):
        print("I'm a car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Similar to a Car!")
    def need_a_push(self):
        print("A little help here?")

give_me_a_car = Car()
give_me_a_yugo = Yugo()

give_me_a_yugo.need_a_push()

# this is an error
# give_me_a_car.need_a_push()