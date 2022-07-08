#pg 183
import os

fin = open('Chapter8/bfile', 'rb')
print(fin.tell())

print(fin.seek(255))

bdata = fin.read()
print(len(bdata))
print(bdata[0])

print(os.SEEK_SET)
print(os.SEEK_CUR)
print(os.SEEK_END)

fin = open('Chapter8/bfile', 'rb')
print(fin.seek(-1,2))
print(fin.tell())

print(len(bdata))
print(bdata[0])