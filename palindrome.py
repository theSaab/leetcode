

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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


    def palindrome(self):
        
        first_letter = self.head
        last_letter = self.head

        if self.head is not None:
            while last_letter is not None:
                last_letter = last_letter.next
        

        if first_letter == last_letter:
            print('here')
        else:
            print('Not palindrome')





Llist.remove_node(3)

print(Llist)