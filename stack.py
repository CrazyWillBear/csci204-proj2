class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        s = ""
        cur_node = self._top

        for _ in range(self._size):
            s += str(cur_node.data) + "->"
            cur_node = cur_node.next

        return s[:-2]

    def push(self, data):
        new_node = Node(data, self._top)
        self._top = new_node
        self._size += 1


    def pop(self):
        if self._top == None:
            return None
        
        node = self._top
        self._top = node.next

        self._size -= 1
        return node.data

    def peek(self):
        return self._top.data if self._top != None else None
        