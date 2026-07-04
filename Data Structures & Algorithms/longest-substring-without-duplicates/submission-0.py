""" brute-force: from each letter go until find no duplicates -> O(n^2)

sliding window:
- init window: l = r = 0
- add in seen set as we go if no duplicates at r
- if encounter duplicate at r, update max_res, move l until theres no more duplicate
- go until r out of bounds
 """

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        window = set()
        res = 0

        while r < len(s):
            while s[r] in window and l < r:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            res = max(r - l + 1, res)
            r += 1

        return res