bdata = bytes(range(0, 256))

fout = open('Chapter8/bfile', 'wb')
size = len(bdata)

offset = 0
chunk = 100

while True:
    if offset > size:
        break
    print(fout.write(bdata[offset:offset+chunk]))
    offset += chunk
    #print(fout.write(bdata[offset:offset+chunk]))
    print(offset, chunk, len(bdata))

fout.close()