RELRO - Relocation Read Only

We need to ensure that the linker resolves all dynamically linked functions at the beginning of the execution, and then makes the GOT read-only.  This technique is called RELRO and ensures that the GOT cannot be overwritten in vulnerable ELF binaries.

## source

https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
