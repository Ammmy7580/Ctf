from pwn import *


#flag - str [A-z0-9{}_]

presentchr = ""
url = "misc.game.alcapwnctf.in"
port =  9089

p = connect(url,port)

print(p.recvuntil('Select: '))

#for A-z
t = 65
while(t<126):
	if t > 90 and t < 97 and t != 95:
		t += 1
		continue
	p.sendline('2')
	p.recvuntil('Rule: ')
	payload = 'flag contains "' + chr(t) + '"'
	p.sendline(payload)
	print("[+]Trying "+str(chr(t))+" ..")
	if p.recvuntil("Welcome")[8] == "F" :
		print("False")
	else :
		print("True")
		presentchr += chr(t)
	p.recvuntil('Select: ')
	t += 1



#for 0-9
t = 48
while(t<58):
	p.sendline('2')
	p.recvuntil('Rule: ')
	payload = 'flag contains "' + chr(t) + '"'
	p.sendline(payload)
	print("[+]Trying "+str(chr(t))+" ..")
	if p.recvuntil("Welcome")[8] == "F" :
		print("False")
	else :
		print("True")
		presentchr += chr(t)
	p.recvuntil('Select: ')
	t += 1

flag = "evlz{"
t = 0

while(True):
	if t==5 :
		break;
	for c in presentchr :
		string = flag + c
		p.sendline('2')
		p.recvuntil('Rule: ')
		payload = 'flag contains "' + string + '"'
		p.sendline(payload)
		if p.recvuntil("Welcome")[8] != "F" :
			flag += c
			print(flag)
			if c == "}":
				t = 5
		p.recvuntil('Select: ')

print(flag)