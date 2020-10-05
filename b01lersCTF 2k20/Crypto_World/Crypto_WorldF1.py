from sympy import *

l = 1200
r = 1500
cnt = 0

for i in range(l,r+1):
	if isprime(i)==True:
		cnt += 1

print(cnt)