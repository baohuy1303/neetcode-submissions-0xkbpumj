''' all words same len
lowercase O(26), unique words

turn beginWord into any word but that word changes 1 char only. then change that word to another as well.
do this inf times until == endWord

check if endWord in wordList -> needs to be in it

a tree with root as endWord and childrens are transformations, each level transforming only 1 char

how do we build the tree?
    - root as endWord
    - from root we check every word in the wordList and we append to seen
        + for each word vs root check, we check if the word has 2 char same. if true: append as child
    - after going thru wordList, we go thru roots child.
    
    - at every word check, we see if the cur word has 2 same char as beginWord, if true: we return level
    how do we keep track of levels?
        - 
 '''
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def check_word(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                if count >= 2:
                    return False
            return True

        q = deque()
        q.append(endWord)
        seen = set(endWord)
        level = 0
        num_nodes_level = 1
        while q:
            cur = q.popleft()
            num_nodes_level -= 1

            if check_word(beginWord, cur):
                return level + 2

            for word in wordList:
                if word in seen:
                    continue
                if check_word(word, cur):
                    q.append(word)
            
            if num_nodes_level == 0:
                level += 1
                num_nodes_level = len(q)

            seen.add(cur)
        
        return 0
            