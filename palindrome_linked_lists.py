

from collections import deque


class LinkedList:   # Basic LinkedLists creation class
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:   # also basic Node creation
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data
      

    def __repr__(self):
        return self.data

list1 = LinkedList(['4', '3', '2', '1', '2', '3', '4'])

def getCount(self): 
        temp = self.head # Initialise temp 
        count = 0 # Initialise count 
  
        # Loop while end of linked list is not reached 
        while (temp): 
            count += 1
            temp = temp.next
        return count 

for node in list1:
    print(node.prev)

# identify start of left and right
left = list1.head
right = getCount(list1)

print(left)
print(right)
