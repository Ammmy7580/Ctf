# You can install these packages to help w/ solving unless you have others in mind
# i.e. python3 -m pip install {name of package}
from pwn import *
import codecs
from base64 import b64decode
from string import ascii_lowercase

dict1 = ['aaaaa', 'aaaab', 'aaaba', 'aaabb', 'aabaa', 'aabab', 'aabba', 'aabbb', 'abaaa',
            'abaab', 'ababa', 'ababb', 'abbaa', 'abbab', 'abbba', 'abbbb', 'baaaa', 'baaab',
            'baaba', 'baabb', 'babaa', 'babab', 'babba', 'babbb', 'bbaaa', 'bbaab']

HOST = 'chal.ctf.b01lers.com'
PORT = 2008

r = remote(HOST,PORT)

def bacon(s):
    output = ''
    j = 0
    while j<len(s) :
        t = s[j:j+5]
        t = t.lower()
        p = 0
        for i in range(len(dict1)) :
            if dict1[i] == t :
                p = i
                break
        output += chr(p+97)
        j += 5

    return output

def rot13(s):
    output = ''
    for c in s :
        output += chr(((ord(c)-97)+13)%26+97)
    return output 

def atbash(s):
    output = ''
    for c in s:
        output += chr((25-ord(c)+97)+97)
    return output

def Base64(s):
    return codecs.decode(b64decode(s))

if __name__ == '__main__':
    count = 0
    while True:     
        r.recvuntil('Method: ')
        method = r.recvuntil('\n').strip()
        r.recvuntil('Ciphertext: ')
        argument = r.recvuntil('\n').strip()
        print(method, argument)
        result = globals()[method.decode()](argument.decode())  # :)

        r.recv()
        r.sendline(result.encode())
        count += 1
        if count == 1000:
            print(r.recv())
            exit(0)
