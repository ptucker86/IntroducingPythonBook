import itertools
count = 0

for item in itertools.chain([1,2],['a', 'b']):
    print(item)

for item in itertools.cycle([1,2]):
    print(item)
    count += 1
    if count == 5:
        print("Counts at 5")
        break

for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)