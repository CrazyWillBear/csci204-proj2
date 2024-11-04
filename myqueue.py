from stack import Node

class LinkedQueue():
    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __len__(self):
        return self._size

    def __str__(self):
        if self._size == 0:
            return "empty queue"

        s = "front --> "

        cur_node = self._front
        for _ in range(self._size):
            s += str(cur_node.data) + " "

        return s + "<-- back"

    def enqueue(self, data):
        """
        The Big-O of this enqueue function is O(1), because it requires a finite number of steps no matter what.
        """
        if self._size == 0:
            self._front = self._back = Node(data)
        else:
            new_node = Node(data)
            self._back.next = new_node
            self._back = new_node

        self._size += 1

    def dequeue(self):
        """
        The Big-O of this enqueue function is O(1), because it requires a finite number of steps no matter what.
        """
        if self._size == 0:
            return None

        node = self._front
        self._front = node.next

        self._size -= 1
        return node.data

    def peek(self):
        if self._size == 0:
            return None

        return self._front.data