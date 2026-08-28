class Solution:
    def isPalindrome(self, s: str) -> bool:
        iterate = []
        for c in s:
            if c.isalnum():
                iterate.append(c.lower())

        l = 0
        r = len(iterate) - 1

        while l < r:
            if iterate[l] != iterate[r]:
                return False
            l += 1
            r -= 1

        return True
        