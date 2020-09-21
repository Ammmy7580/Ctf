p = "IAJBO{ndldie_al_aqk_jjrnsxee}"

offset = 21
for c in p:
	i = ord(c)
	if i>=65 and i<=90 :
		i = i-65
		i = (i+offset)%26 + 65
		print(chr(i),end="")
		offset -=1

	elif i>=97 and i<=122:
		i = i-97
		i = (i+offset)%26 + 97
		print(chr(i),end="")
		offset -=1

	else :
		print(c,end="")
		offset -=1

print()