# linked list ds to store lru cache
class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cache = defaultdict(int)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self, node):
        prev_node = self.right.prev
        next_node = self.right

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val

        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
