class Node:
    """A node of a linked list"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, node_data):
        """Set node data"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, node_next):
        """Set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        """String"""
        return str(self._data)


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        current = self.head
        previous = None
        temp = Node(item)
        while current is not None and current.data < item:
            previous = current
            current = current.next
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                return False
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None
        while current is None:
            if current.data == item:
                break
            previous = current
            current = current.next
        if current is None:
            raise ValueError("f{item} is not in the list")
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None

    def reverse(l):
        if l.head is None:
            return

        current_node = l.head
        prev_node = None

        while current_node is not None:
            # Track the next node
            next_node = current_node.next

            # Modify the current node
            current_node.next = prev_node

            # Update prev and current
            prev_node = current_node
            current_node = next_node

        l.head = prev_node

    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def __str__(self) -> str:
        current = self.head
        string = ""
        while current is not None:
            string += f"{current.data}, "
            current = current.next
        return string
