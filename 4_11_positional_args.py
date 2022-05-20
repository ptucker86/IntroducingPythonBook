def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

#print(menu('chardonnary', 'chicken', 'cake'))

#print(menu(wine='malbec', dessert='flan', entree='beef'))

#print(menu(wine='malbec', entree='beef'))

def print_args(*args):
    print('Positional argument tuple:', args)

# print_args()
# print_args(3, 2, 1, 'wait', 'uh...', 5)

def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this too:', required2)
    print('All the rest:', args)

# print_more('cap', 'gloves', 'scarf', 'keys', 'horse')

# docstrings
def echo(anything):
    '''
    printing input stings
    in a text block
    doo doo doo 
    waaah
    '''
    return anything
