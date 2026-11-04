class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.back = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.back = self.head
        self.nodes = {}

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._unlink(node)
        self._append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._unlink(node)
            self._append(node)
            return
        if len(self.nodes) == self.capacity:
            lru = self.head.next
            self._unlink(lru)
            del self.nodes[lru.key]
        node = Node(key, value)
        self.nodes[key] = node
        self._append(node)

    def _unlink(self, node):
        node.back.next = node.next
        node.next.back = node.back

    def _append(self, node):
        node.back = self.tail.back
        node.next = self.tail
        self.tail.back.next = node
        self.tail.back = node