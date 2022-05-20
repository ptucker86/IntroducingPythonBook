# intro to python functions
def do_nothing():
    pass

# do_nothing()

def make_a_sound():
    print('quack')

# make_a_sound()

def agree():
    return True

#if agree():
#    print('Splendid!')
#else:
#    print('DID NOT AGREE')

def echo(anything):
    return anything + ' ' + anything

# print(echo('rumplestitskin'))

def commentary(color):
    if color == 'red':
        return "Its a tomato."
    elif color == "green":
        return "Its a green pepper."
    elif color == 'bee purple':
        return "I think only bees can see this"
    else:
        return "I've never heard of " + color + "."
comment = commentary('orangee')
print(comment)