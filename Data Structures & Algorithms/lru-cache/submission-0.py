class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        # doubly linked list
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0,0) # LRU
        self.right = Node(0,0) # MRU

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        node.prev = prev_node
        node.next = next_node

        prev_node.next = node
        next_node.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move accessed node to MRU (right)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If key exists, remove old node
            self.remove(self.cache[key])

        # Create new node and insert at MRU position
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # If capacity exceeded, evict LRU (node after left dummy)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]