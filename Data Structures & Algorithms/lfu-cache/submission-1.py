from collections import defaultdict

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.next = None
        self.back = None

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.back = self.head
        self.size = 0

    def unlink(self, node):
        node.back.next = node.next
        node.next.back = node.back
        self.size -= 1

    def append(self, node):
        node.back = self.tail.back
        node.next = self.tail
        self.tail.back.next = node
        self.tail.back = node
        self.size += 1

    def pop_head(self):
        node = self.head.next
        self.unlink(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.freqs = defaultdict(DLL)
        self.min_freq = 1

    def move_freq(self, key):
        node = self.nodes[key]
        f = node.freq

        bucket = self.freqs[f]
        bucket.unlink(node)
        if bucket.size == 0:
            del self.freqs[f]
            if self.min_freq == f:
                self.min_freq += 1
        node.freq += 1
        self.freqs[node.freq].append(node)

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        
        node = self.nodes[key]
        self.move_freq(key)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.move_freq(key)
            return

        if len(self.nodes) == self.capacity:
            evict_node = self.freqs[self.min_freq].pop_head()
            if self.freqs[self.min_freq] == 0:
                del self.freqs[self.min_freq]
            del self.nodes[evict_node.key]

        node = Node(key, value)
        self.min_freq = 1
        self.freqs[1].append(node)
        self.nodes[key] = node
        
        
                
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)