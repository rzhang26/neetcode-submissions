class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def appendleft(self, val) -> None:
        """Adds an item to the front (left side) -> O(1)"""
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def append(self, val) -> None:
        """Adds an item to the back (right side) -> O(1)"""
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def popleft(self):
        """Removes and returns an item from the front (left side) -> O(1)"""
        if self.is_empty():
            raise IndexError("popleft from an empty deque")
        
        val_to_return = self.head.val
        
        # If there's only one item left, emptying the deque
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
        self._size -= 1
        return val_to_return

    def pop(self):
        """Removes and returns an item from the back (right side) -> O(1)"""
        if self.is_empty():
            raise IndexError("pop from an empty deque")
            
        val_to_return = self.tail.val
        
        # If there's only one item left, emptying the deque
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            
        self._size -= 1
        return val_to_return

    def peekleft(self):
        """Look at the front item without removing it -> O(1)"""
        return self.head.val if self.head else None

    def peek(self):
        """Look at the back item without removing it -> O(1)"""
        return self.tail.val if self.tail else None
class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        size = len(self.queue)
        self.queue.append(x)

        for i in range(size):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()