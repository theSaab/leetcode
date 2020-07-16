
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


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

    def find_intersection(self, other):
        position = 1
        first = self.head
        second = other.head

        if (self.head is not None and other.head is not None):
            while (first is not None and second is not None):
                if first.data == second.data:
                    print('There is an intersection is at ' + str(position))
                    break
                else:
                    position += 1
                    first = first.next 
                    second = second.next
            
            else:
                print('No intersection')


list1 = LinkedList(['1', '3', '3', '4'])
list2 = LinkedList(['2', '3', '2', '4'])

list1.find_intersection(list2)
