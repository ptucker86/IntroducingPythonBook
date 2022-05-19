marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
print(marxes[0:2])
print(marxes[::2])
## reverse list
print(marxes[::-1])
marxes.append('Zeppo')
print(marxes)

## extend NOT APPEND
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)

print(marxes.pop())
print(marxes.index('Chico'))
print('Groucho' in marxes)