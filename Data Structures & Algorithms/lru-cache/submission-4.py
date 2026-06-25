class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.head = None
        self.tail = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #stores [key: Node] pairs?
        self.capacity = capacity

        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert_at_head(self, node):
        first_real_node = self.head.next

        self.head.next = node
        node.prev = self.head
        node.next = first_real_node
        first_real_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert_at_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert_at_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self.insert_at_head(new_node)

            if len(self.cache) > self.capacity:
                lru_node = self.tail.prev
                self.remove(lru_node) #remove from tree
                del self.cache[lru_node.key] #remove from dict (hash map)

