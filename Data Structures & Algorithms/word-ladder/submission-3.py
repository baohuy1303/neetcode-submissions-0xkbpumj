from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList or beginWord == endWord:
            return 0    

        q = deque()
        q.append(beginWord)
        wordList = set(wordList)
        level = 0
        node_level = 1
        while q:
            cur = q.popleft()
            node_level -= 1
            if cur == endWord:
                return level + 1
            for i in range(len(cur)):
                for j in range(27):
                    char = chr(97 + j)
                    new_word = cur[:i] + char + cur[i+1:]
                    if new_word in wordList:
                        q.append(new_word)
                        wordList.remove(new_word)

            if node_level == 0:
                level +=1
                node_level = len(q)

        return 0