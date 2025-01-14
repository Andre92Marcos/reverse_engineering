from pwn import *
import sys

PATH_TO_BINARY= str(sys.argv[1]) # specify the path to the binary to overflow
p = process(PATH_TO_BINARY)

gdb.attach(p.pid, "c")
payload = cyclic(1000)
p.sendline(payload)
#x/wx $rsp - Search for bytes that crashed the application
#in python cyclic_find(bytes_that_crashed) to find the offset
p.interactive()
exit()

#based on https://book.hacktricks.xyz/misc/basic-python/rop-pwn-template


