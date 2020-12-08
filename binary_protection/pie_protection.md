Position Independent Executables (PIE) are an output of the hardened package build process. A PIE binary and all of its dependencies are loaded into randomized locations within virtual memory each time the application is executed. This makes Return Oriented Programming (ROP) attacks much more difficult to execute reliably.

## source

https://www.redhat.com/en/blog/hardening-elf-binaries-using-relocation-read-only-relro
