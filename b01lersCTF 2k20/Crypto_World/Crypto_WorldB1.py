for i in range(10000):
	n = (179*i)+1
	if n%123==0 :
		print(n)
		break;

print("x = " + str(int(n//123)))
print("y = " + str(int((1-n)//179)))