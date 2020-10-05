# 11^x mod 101 = 27

for i in range(10000000) :
	c = pow(11, i)
	if c%101==27 :
		print(i)
		break