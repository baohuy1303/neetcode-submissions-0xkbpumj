from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        cS = Counter(s)
        cT = Counter(t)

        return cS == cT

        