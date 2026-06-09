''' store and retrieve keys in a set of strings
auto-complete and spell checker systems.

Inserts the string word into the prefix tree.

Search if word in prefix tree
Search if startsWith word in prefix tree

- Each char as a node that points to next char
- Search word:
    - dict key (first_char) : list(words that start with it)
        + O(1) to search for the word
        + O(len_list) to search for startsWith
        -> Worst case O(n)

    - dict key (firstchar) : firstchar_node (Find startsWith?) 
        + O(word) to find if a word is in or not - Worst case O(26) ~ O(1)

    TreeNode: next_chars: {o: Node(), g: Node()}
 '''
class Node:
    def __init__(self, next_chars, end=False):
        self.next_chars = {}
        self.end = end

class PrefixTree:

    def __init__(self):
        self.root = Node(next_chars={})

    def insert(self, word: str) -> None:
        cur = self.root
        for i in range(0, len(word)):
            if word[i] not in cur.next_chars:
                cur.next_chars[word[i]] = Node({})
            cur = cur.next_chars[word[i]]
        cur.end = True
        return

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(0, len(word)):
            if word[i] not in cur.next_chars:
                return False
            cur = cur.next_chars[word[i]]
        if cur.end == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(0, len(prefix)):
            if prefix[i] not in cur.next_chars:
                return False
            cur = cur.next_chars[prefix[i]]
        return True
        