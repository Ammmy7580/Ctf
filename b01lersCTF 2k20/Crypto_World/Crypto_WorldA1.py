# 299*x + 355*y + 251*z = 0


for z in range(1000) :
	for y in range(1000) :
		c = 355*y + 251*z
		if (c%299==0) :
			print('- + +  OR  + - -')
			x = c//299
			print(y,z,x)
			break


for z in range(1000) :
	for y in range(1000) :
		c = 355*y - 251*z
		if (c%299==0) :
			print('- - +  OR  + + -')
			break