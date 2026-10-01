class Node:
    def __init__(self):
        self.next = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node()
            cur = cur.next[c]
        cur.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i >= len(word):
                return node.is_word
            
            c = word[i]
            if c == ".":
                for k, v in node.next.items():
                    if dfs(i+1, v):
                        return True
                return False
            
            if c not in node.next:
                return False
            return dfs(i+1, node.next[c])

        return dfs(0, self.root)