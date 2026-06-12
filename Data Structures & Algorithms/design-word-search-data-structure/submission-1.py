''' adding new words and searching for EXISTING words

addWord(word) Adds word to the data structure

search(word) return True if any matches word, else False
dots '.' is any letter. There will be at most 2 dots in word for search queries

word: lowercase Eng letter (26)

add word into a set. see if word in set or not
BUT this wouldnt be possible with '.'

brute force: we check char by char at each index of the word.
O(num_of_words * word_length)

There will be at most 2 dots in word for search queries.
we use a Trie Node, and whenever we see a dot, we just check every word at the next level to see if it matches
since theres only 2 dots -> O(26^2 * n) ~ O(n)

each node represents a char

- dots need to match word length '''

class Node:
    def __init__(self):
        self.childrens = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.childrens:
                cur.childrens[c] = Node()
            cur = cur.childrens[c]
        cur.end = True

    def search(self, word: str) -> bool:

        def dfs(index, node):
            cur = node

            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for child in cur.childrens.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.childrens:
                        return False
                    cur = cur.childrens[c]
                
            return cur.end

        return dfs(0, self.root)

        
