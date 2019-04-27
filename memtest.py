from objsizer import getsize
import os
import helloworld


class A:
    count=1
    name="Class A"
    
    def __init__(self):
        self.data = []


class B:
    buffer = bytearray(os.urandom(1024*1024))

class C:
    a = A()
    b = B()

anA = A()
aB = B()
aC = C()

print ("size of anA is ",str(getsize(anA)))
print ("size of aB is ",str(getsize(aB)))
print ("size of aC is ",str(getsize(aC)))

print helloworld.helloworld()

