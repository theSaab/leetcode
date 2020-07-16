
# This program takes 2 linked lists, list 1 and list2, and where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.


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
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


def create_num(self):
    # This function turns the linked list into a number to be used later
    num = ''
    for node in self:
        if node != None:  
            num = str(node) + num
    return int(num)


def add_nums(first, second):
    # this function takes 2 numbers and returns the addition as a string
    list_sum = []
    num3 = str(first + second)

    for char in num3[len(num3)::-1]:
        list_sum.append(char)

    print(list_sum)

    # presents the linked list, final product
    print(LinkedList(list_sum))


def sum_lists(list1, list2):
    list1 = LinkedList(list1)
    list2 = LinkedList(list2)

    num1 = create_num(list1)
    num2 = create_num(list2)

    add_nums(num1, num2)


sum_lists(['7', '1', '6'], ['5', '9', '2'])
