guess_me = 7
if guess_me < 7:
    print("too low")
elif guess_me > 7:
    print("too high")
else:
    print("just right")

start = 1
while start < guess_me:
    print("too low")
    start += 1
else:
    if start == guess_me:
        print("found it")
    else:
        print('oops')

x43 = [3, 2, 1, 0]
for x in x43:
    print(x)