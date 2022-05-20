def get_description():
    """ Return random weather"""
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'APOCOLYPSE']
    return choice(possibilities)