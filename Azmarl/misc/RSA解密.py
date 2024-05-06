import gmpy2

p=gmpy2.mpz(3)
q=gmpy2.mpz(11)
e=gmpy2.mpz(3)
l=(p-1)*(q-1)
d=gmpy2.invert(e,l)
c=gmpy2.mpz(26)
n=p*q
ans=pow(c,d,n)
print ans