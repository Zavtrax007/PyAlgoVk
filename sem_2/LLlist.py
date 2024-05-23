class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return self.head
        new_node.next = self.head
        self.head = new_node

    def append_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next

        cur_node.next = new_node

    def print_list(self):
        cur_node = self.head
        output = ""
        while cur_node is not None:
            output += str(cur_node.data)
        if cur_node.next:
            output += " -> "
        cur_node = cur_node.next
        print(output)

    def insert(self,linkedList, after, n):
        search = linkedList.head
        while search is not None:
            if search.data == after:
                break

        search = search.next

        if search is not None:
            node = Node
            node.data = n
        if search == tail:
            tail = node
        node.next = search.next
        search.next = node