#global variable
animal = 'fruitbat'
def print_global():
    print('inside the print_global function:', animal)

print('at the actual global level:', animal)
print_global()

# def change_and_print_global():
    # print("inside change_and_print_global:", animal)
    # animal = 'wombat'
    # print('after the animal change', animal)

# print(change_and_print_global())

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
print(animal)
print(id(animal))

def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change and print global:', animal)

print(animal)
print(id(animal))
change_and_print_global()
print(animal)
print(id(animal))


# name space dunders
def amazing():
    ''' 
    This is amazing
    what else can I do
    anything I want'''
    print('This function is name:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()