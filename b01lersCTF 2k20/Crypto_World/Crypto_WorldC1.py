# x^2 mod 97 = 88
import math 

def isPerfectSquare(x): 
    sr = math.sqrt(x)
    return ((sr - math.floor(sr)) == 0) 


for i in range(100000) :
	c = 97*i + 88
	if isPerfectSquare(c) :
		print(math.sqrt(c))
		break