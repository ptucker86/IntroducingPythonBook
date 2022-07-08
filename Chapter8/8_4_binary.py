bdata = bytes(range(0,256))
print(len(bdata))

fout = open('Chapter8/bfile', 'wb')
fout.write(bdata)

fout.close()