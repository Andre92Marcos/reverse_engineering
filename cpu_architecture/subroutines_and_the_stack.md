Before starting the execution of a subroutine the call instruction pushes the return address onto the stack (and the rip points to it) then jumps to the address of the beginning of the subroutine.

the return instruction sets rsp to rbp thus releasing the space allocated to the subroutine. It pops the return address from the stack into rip thus resuming the executio at the saved return address
