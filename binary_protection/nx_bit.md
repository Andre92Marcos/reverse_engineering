It marks a memory page non-executable in the virtual memory system and in the TLB (a structure used by the CPU for resolving virtual memory mappings). If any program code is going to be executed from such page, the CPU will fault and transfer control to the operating system for error handling.

Programs normally have their binary code and static data in a read-only memory section and if they ever try to write there, the CPU will fault and then the operating-system normally kills the application (this is known as segmentation fault or access violation).

For security reasons, the read/write data memory of a program is usually NX-protected by default. This prevents an attacker from supplying some application his malicious code as data, making the application write that to its data area and then having that code executed somehow, usually by a buffer overflow/underflow vulnerability in the application, overwriting the return address of a function in stack with the location of the malicious code in the data area.

# source

https://stackoverflow.com/questions/2168555/how-does-the-nx-flag-work
