poem = ''
print(len(poem))

fin = open('Chapter8/relativity.txt', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

#poem = fin.read()
fin.close()

print(len(poem))
print(poem)