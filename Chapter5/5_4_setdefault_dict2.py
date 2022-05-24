from collections import defaultdict
from email.policy import default

def no_idea():
    return 'Huh?'

# bestiary = defaultdict(no_idea)
# bestiary['A'] = 'Abominable Snowman'
# bestiary['B'] = 'Basilisk'
# print(bestiary['A'])
# print(bestiary['B'])
# print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])

food_counter = defaultdict(int)
for food in ['spam','spam','eggs','spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)
