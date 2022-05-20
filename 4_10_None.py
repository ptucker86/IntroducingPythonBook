# playing with None
thing = None

#evaluated as a bool
if thing:
    print("it's something")
else:
    print("it's no thing")

#use as operator
if thing is None:
    print("It's nothing")
else:
    print("It's something")

#Is it a bool or a none
def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none(0)
# print(is_none([]))
# print(is_none(set()))
# print(is_none(list()))
