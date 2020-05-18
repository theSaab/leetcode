
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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Llist = LinkedLists()

num1_1 = Node(deque(123))
num1_2 = Node(2)
num1_3 = Node(3)
num2_1 = Node(4)
num2_2 = Node(5)
num2_3 = Node(6)

num1_1.next = num1_2
num1_2.next = num1_3

num2_1.next = num2_2
num2_2.next = num2_3

first_node = num1
Llist.head = first_node





for elem in Llist:
    print(elem.data)