from typing import List


a_set = {number for number in range(1,6) if number % 3 == 1}
print(a_set)

number_thing = (number for number in range(1,6))
#print(type(number_thing))
#for number in number_thing:
#    print(number)

number_list = list(number_thing)
print(number_list)