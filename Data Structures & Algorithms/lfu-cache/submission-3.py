class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1

        self.next = None
        self.prev = None

class LRU:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def pop_lru(self):
        node = self.head.next
        self.unlink(node)
        return node

    def unlink(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev
        self.size -= 1

    def add_to_end(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node

        node.next = self.tail
        node.prev = prev
        self.size += 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.use_bucket = defaultdict(LRU) # freq/counter -> Linkedlist
        self.min_freq = 0

        self.keys = {}

    def move_to_new_bucket(self, node):
        old_bucket = self.use_bucket[node.freq]
        old_bucket.unlink(node)
        if old_bucket.size == 0:
            if node.freq == self.min_freq:
                self.min_freq += 1
            
            del self.use_bucket[node.freq]
        
        node.freq += 1
        new_bucket = self.use_bucket[node.freq]
        new_bucket.add_to_end(node)


    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self.move_to_new_bucket(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.keys:
            node = self.keys[key]
            node.value = value
            self.move_to_new_bucket(node)
            return

        if self.capacity == self.size:
            min_bucket = self.use_bucket[self.min_freq]
            lru = min_bucket.pop_lru()
            self.size -= 1
            del self.keys[lru.key]
            if min_bucket.size == 0:
                del self.use_bucket[self.min_freq]
        
        node = Node(key, value)
        self.use_bucket[1].add_to_end(node)
        self.keys[key] = node
        self.min_freq = 1
        self.size += 1
        return


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)