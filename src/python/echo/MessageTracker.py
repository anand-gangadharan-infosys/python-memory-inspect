import os
import helloworld


class MessageTracker:
    #static collections
    memoryHole=[]
    messages=[]

    def addMessage(self,msg):
        MessageTracker.messages.append(msg)
        fatObj=MyFatObject()
        MessageTracker.memoryHole.append(fatObj)
        MessageTracker.memoryHole.append(bytearray(os.urandom(500*1024)))

    def removeMessage(self,msg):
        MessageTracker.messages.remove(msg)

    def printMessages(self):
        i=1
        for msg in MessageTracker.messages:
            print ("Message ",str(i), ":", msg)
            helloworld.helloworld()

class MyFatObject:
    def __init__(self):
        self.buff = bytearray(os.urandom(1024*1024))



