from sympy import *

l = pow(10, 400)
r = pow(10, 500)
cnt = 0
print(l)
for i in range(l,r+1):
	if isprime(i)==True :
		cnt += 1

	if cnt==16 :
		print(i)
		break

print(cnt)