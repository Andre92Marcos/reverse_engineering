Stack canaries are used to detect a stack buffer overflow before exectuion of malicous code can occur.

This method works by placing a small integer, the value of which is randomly chosen at program start, in memory just before the stack return pointer.

Most buffer overflows overwrite memory from lower to higher memory addresses, so in order to overwrite the return pointer (and thus take control of the process) the canary value must also be overwritten.

This value is checked to make sure it has not changed before a routine uses the return pointer on the stack.

This technique can greatly increase the difficulty of exploiting a stack buffer overflow because it forces the attacker to gain control of the instruction pointer by some non-traditional means such as corrupting other important variables on the stack.

#source https://en.wikipedia.org/wiki/Stack_buffer_overflow#Stack_canaries
https://ctf-wiki.github.io/ctf-wiki/pwn/linux/mitigation/canary/
