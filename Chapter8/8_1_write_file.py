poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

print(len(poem))

try:
    fout = open('Chapter8/relativity.txt', 'xt')
    fout.write('stomp')
    # fout.write(poem)
    #print(poem, file=fout, sep='', end='')
except FileExistsError:
    print('relativity already exists!')

size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
#    print(len(fout.write(poem[offset:offset+chunk])))
    offset += chunk
fout.close()