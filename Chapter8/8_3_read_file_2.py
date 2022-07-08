#page 181

# poem = ''

fin = open('Chapter8/relativity.txt', 'rt')
# for line in fin:
#    poem += line
lines = fin.readlines()
fin.close()

#print(len(poem))
print(len(lines), 'lines read')

for line in lines:
    print(line, end='')
