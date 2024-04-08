s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
key = 'KVQP0LdJKRaV3n9D'
m = ''
for i in key:
    for j in range(len(s)):
        if i == s[j]:
            m += "{} {} 0 {} ".format(j,j,len(s)-1)
print(m)