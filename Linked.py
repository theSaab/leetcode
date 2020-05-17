

graph = {
    1: [2, 3, None],
    2: [4, None],
    3: [None],
    4: [5, 6, None],
    5: [6, None],
    6: [None]
}


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

    def add_last(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)
    
    def add_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)






class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


Llist = LinkedLists()

first_node = Node('saba')
Llist.head = first_node

second_node = Node('abas')
third_node = Node('pars')
fourth_node = Node('john')
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node

Llist.add_first(Node('bruh'))
Llist.add_last(Node('hello'))

Llist.add_after('abas', Node('mandems'))
Llist.add_before('bruh', Node('pullers'))

for node in Llist:
    print(node.data)
