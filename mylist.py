from stack import Node
from items import SparePart, ShipPiece

class MyList:
    def __init__(self):
        self._top = None
        self._size = 0

    def __str__(self):
        if self._size == 0:
            return "empty list"

        s = "["
        cur_node = self._top

        for _ in range(self._size):
            s += str(cur_node.data) + ", "
            cur_node = cur_node.next

        return s[:-2] + "]"

    def __len__(self):
        return self._size

    def insert(self, data, index=-1):
        # if index is negative or too large put it at end
        if index < 0 or index > self._size:
            index = self._size

        if self._top == None:  # new list
            self._top = Node(data)
        elif index == 0:
            new_node = Node(data, self._top)
            self._top = new_node
        else:  # existing list
            # traverse linked list
            cur_node = self._top
            for _ in range(index - 1):
                cur_node = cur_node.next

            # insert node
            new_node = Node(data, cur_node.next)
            cur_node.next = new_node

        self._size += 1  # increment size

    def delete(self, index):
        # if index is out of range or the list is empty
        if index < 0 or index >= self._size or self._top is None:
            return None

        # deleting the head (first node)
        if index == 0:
            node = self._top
            self._top = self._top.next
        else:
            # traverse linked list to find the node before the target node
            cur_node = self._top
            for _ in range(index - 1):
                cur_node = cur_node.next

            # remove node
            node = cur_node.next
            cur_node.next = node.next

        self._size -= 1  # decrement size
        return node.data  # return the node's data


    def count(self, data):
        count = 0

        # traverse linked list
        cur_node = self._top
        for i in range(self._size):
            # if node's data matches, remove it
            if cur_node.data == data:
                count += 1

            cur_node = cur_node.next

        return count

    def countPartsWithName(self, name):
        count = 0

        # traverse linked list
        cur_node = self._top
        for i in range(self._size):
            # if node's data matches, remove it
            if cur_node.data.getName() == name:
                count += 1

            cur_node = cur_node.next

        return count

    def find(self, data):
        """
        The Big-O of this is O(n), as it requires list traversal. This means the number of steps
        depends on the size of the list, n. It should be this, since I chose to use a LinkedList
        implementation instead of an array.
        """
        # traverse linked list
        cur_node = self._top
        for i in range(self._size):
            # if node's data matches, remove it
            if cur_node.data == data:
                return i

            cur_node = cur_node.next

        return -1  # return -1 if not found

    def findPartWithName(self, name):
        """
        The Big-O of this is O(n), as it requires list traversal. This means the number of steps
        depends on the size of the list, n. It should be this, since I chose to use a LinkedList
        implementation instead of an array.
        """
        # traverse linked list
        cur_node = self._top
        for i in range(self._size):
            # if node's data matches, remove it
            if cur_node.data.getName() == name:
                return i

            cur_node = cur_node.next

        return -1  # return -1 if not found

    def remove(self, data):
        # find the data
        index = self.find(data)

        if index != -1:
            self.delete(index)

    def peek(self, index):
        # if index is negative, too large, or if list is empty
        if index < 0 or index >= self._size or self._size == 0:
            return None

        # traverse linked list
        cur_node = self._top
        for _ in range(index):
            cur_node = cur_node.next

        return cur_node.data
            
if __name__ == "__main__":
    gear1 = SparePart("gear.ppm")
    gear2 = SparePart("gear.ppm")
    gear3 = SparePart("gear.ppm")
    gear4 = SparePart("gear.ppm")

    l = MyList()
    l.insert(gear1)
    l.insert(gear2)
    l.insert(gear3)
    l.insert(gear4)

    print(l)