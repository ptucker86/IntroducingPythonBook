accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
'person': 'Col. Mustard'}

for card in accusation:
    print(card)

# commenting out
# count = 1
# while count <=5:
#     print(count)
#     count += 1

# while True:
#    stuff = input("String to capitalize [type q to quit]:")
#    if stuff == "q":
#        break
#    print(stuff.capitalize())

numbers = [1, 3, 5, 7]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else: #no break called
    print('No even number found')

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
for rabbit in rabbits:
    print(rabbit)

