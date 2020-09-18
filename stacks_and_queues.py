

# making a stack using queue functions,
# making a queue using stack functions,


class Stack:

    def __init(self):

        self.queueOG = []
        self.queueSpare = []

    def isEmpty(self):

        return self.queueOG == []
    
    def peek(self):

        return self.queueOG[-1]

    def pop(self):

        for i in range(len(self) - 1):
            self.queueSpare.enqueue(self.queueOG.dequeue())

        self.queueOG, self.queueSpare = self.queueSpare, self.queueOG

        return self.queueSpare.dequeue()

    def push(self, element):

        self.queueSpare.enqueue(element)
        for i in range(len(self)):
            self.queueSpare.enqueue(self.queueOG.dequeue())

        self.queueOG, self.queueSpare = self.queueSpare, self.queueOG



class Queue :

    def __init__(self):

        self.stackOG = []
        self.spare = []

    def isEmpty(self):
        return self.isEmpty()

    def enqueue(self, element):
            self.stackOG.push(element)

    def dequeue(self):

        while self.stackOG.isEmpty() == False:
            
            self.spare.push(self.stackOG.pop())
            
        return self.spare.pop()
