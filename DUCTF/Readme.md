****DUCTF****<br/><br/>


***Formating (Reversing)***<br/>
I opened this binary in gdb and keep an eye over the values which pushed into the stack.
And got the flag in hex format.(Decode it into String)<br/><br/>

***shellthis (PWn)***<br/>
In this binary we have to just redirect the code execution.<br/>
Fristly, I calculated the EIP offset (after how many bytes I overflowed the buffer).<br/>
Then, Using the Pwntools I ma able to find the address of get_shell function.<br/>
Finally run the shellthis.py over the remote server of duc.tf<br/><br/>

***rot-i (Crypto)***<br/>
As a hint We already know first 6 letter are 'DUCTF{'.<br/>
So, I calculated the jump for first letter to become D it is (21).<br/>
For 2nd letter it is (20), for next letter it is (19) and so on.....<br/>
I observed the pattern, And wrote a script to decrypt the cipher.<br/>


****Thank You****
