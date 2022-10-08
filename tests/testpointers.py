from pointers import c_malloc as malloc 
from pointers import to_ptr
from pointers import Struct


name = "Unity"
pname = to_ptr(name)
name = "Current"
tname = pname.dereference()

print(name)
print(pname)
print(tname)

class DivT(Struct):
    quot: int

