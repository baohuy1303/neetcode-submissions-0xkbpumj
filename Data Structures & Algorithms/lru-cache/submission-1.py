class Node:
    def __init__(self, key, value):
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

        self.nodes = {} # key -> node

    def unlink(self, node):
        prev = node.back
        next_node = node.next
        prev.next = next_node
        next_node.back = prev

    def put_to_front(self, key):
        node = self.nodes[key]
        if node.back:
            self.unlink(node)

        prev = self.tail.back
        prev.next = node
        self.tail.back = node

        node.back = prev
        node.next = self.tail

    def remove_last(self):
        del self.nodes[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.back = self.head

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        self.put_to_front(key)
        return self.nodes[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            if len(self.nodes) == self.capacity:
                self.remove_last()
            self.nodes[key] = Node(key, value)
        else:
            self.nodes[key].value = value
        
        self.put_to_front(key)
        return
        
