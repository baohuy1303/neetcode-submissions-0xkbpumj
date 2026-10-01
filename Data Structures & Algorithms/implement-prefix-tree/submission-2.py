class Node:
    def __init__(self, letter=""):
        self.letter = letter
        self.next = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c in cur.next:
                cur = cur.next[c]
                continue
                
            cur.next[c] = Node(c)
            cur = cur.next[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]

        if cur.is_word:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        
        return True