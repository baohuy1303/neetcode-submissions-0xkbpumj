class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # have to be next to eachother
        # each step decide where to cut
        # include 1, 2, 3 chars etc... have helper to check palindrome
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []
        def cut(start, path):
            if start >= len(s):
                res.append(path)
                return

            for i in range(len(s) - start):
                end = start + i
                if isPalindrome(start, end):
                    path.append(s[start:end+1])
                    cut(end+1, path.copy())
                    path.pop()
            
            return
        cut(0, [])
        return res