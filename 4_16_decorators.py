def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

@square_it
@document_it
def add_ints(*args):
    return sum(args)

print(add_ints(3,10))

#cooler_add_ints = document_it(add_ints)

#print(cooler_add_ints(7,9,10,13))
