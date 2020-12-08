When using FORTIFY_SOURCE the compiler will try to intelligently read the code it is compiling / building.

When it sees a C-library function call against a variable whose size it can deduce (like a fixed-size array - it is more intelligent than this btw) it will replace the call with a FORTIFY'ed function call, passing on the maximum size for the variable.

If this special function call notices that the variable is being overwritten beyond its boundaries, it forces the application to quit immediately.

If this special function call notices that the variable is being overwritten beyond its boundaries, it forces the application to quit immediately.

## source

https://blog.siphos.be/2011/07/high-level-explanation-on-some-binary-executable-security/
