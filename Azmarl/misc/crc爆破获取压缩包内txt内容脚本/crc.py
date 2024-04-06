import zipfile
import string
import binascii

string=string.printable
crc_s=''
for i in range(0,68):
    zip_name= "out" + str(i) + ".zip"    #读每个文件
    zip_crc=zipfile.ZipFile(zip_name,'r').getinfo('data.txt').CRC
    #读crc
    print(zip_crc)
    for a in string:
        for b in string:
            for c in string:
                for d in string:
                    s=a+b+c+d
                    #进行爆破
                    if zip_crc == (binascii.crc32(s.encode())):
                        print(s)
                        crc_s+=s
print(crc_s)