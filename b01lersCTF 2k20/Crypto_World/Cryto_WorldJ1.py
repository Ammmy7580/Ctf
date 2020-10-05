import math 
  
def isPerfectSquare(x): 
    sr = math.sqrt(x)
    return ((sr - math.floor(sr)) == 0) 

x=0
y=0
for i in range(1000):
	c = i*i*22
	if(isPerfectSquare(8383-c)):
		y = i
		x = math.sqrt(8383-c)
		print(x,y)
		print(i)
		break

