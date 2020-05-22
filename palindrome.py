

from collections import deque

class LinkedLists:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def palindrome(self):
        list = deque(self)
        blank = deque()
        for node in list:
            blank.add_first(node)
        
        if blank == self:
            print('here')
        print(blank)
        print(list)  
 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


Llist = LinkedLists()

first_node = Node('1')
Llist.head = first_node
Llist.head.next = Node('2')
Llist.head.next.next = Node('3')
Llist.head.next.next.next = Node('2')
Llist.head.next.next.next.next = Node('1')


Llist.palindrome()