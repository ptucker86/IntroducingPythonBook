from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
lunch = ['eggs', 'eggs', 'bacon']

breakfast_counter = Counter(breakfast)
print(breakfast_counter)

lunch_counter = Counter(lunch)
print(lunch_counter)

print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))

full_orders = breakfast_counter + lunch_counter
print(full_orders)

less_orders = breakfast_counter - lunch_counter
print(less_orders)

intersecting_orders = breakfast_counter & lunch_counter
print(intersecting_orders)

union_orders = breakfast_counter | lunch_counter
print(union_orders)