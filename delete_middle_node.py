

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

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):

                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next

            return slow_ptr.data

    def remove_middle(self):

        middle = self.find_middle()
        self.remove_node(middle)

        for elem in self:
            print(elem.data)


Llist = LinkedLists([1, 2, 3, 'middle', 5, 6, 7])

Llist.remove_middle()