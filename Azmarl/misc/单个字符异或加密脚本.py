f1 = open('./cipher','r')
xor_data = f1.read()
f1.close()
dec_data = ""
for i in xor_data:
    tmp = int(i,16) ^ 5
    dec_data += hex(tmp)[2:]
f2 = open('./data.doc','wb')
f2.write(dec_data.decode('hex'))
f2.close()