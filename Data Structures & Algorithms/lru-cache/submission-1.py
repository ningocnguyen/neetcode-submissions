class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity

        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        next_node = node.next
        prev_node = node.prev

        next_node.prev = prev_node
        prev_node.next = next_node
        
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        node.next = next_node
        node.prev = prev_node

        next_node.prev = node
        prev_node.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node # overwrite

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)