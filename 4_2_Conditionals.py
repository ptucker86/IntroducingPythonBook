disaster = False

if disaster:
    print("Woe!")
else:
    print("Whee!")

x = 7
print(x == 5)
print(x == 7)
print(5 < x)
print(10< x)


some_list = []
if some_list:
    print("There's something in here")
else:
    print("Hey, it's empty!")


vowels = 'aeiou'
letter = 'o'
print(letter in vowels)
if letter in vowels:
    print(letter, 'is a vowel')