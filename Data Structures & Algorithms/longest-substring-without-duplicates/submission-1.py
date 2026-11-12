class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        res = 0
        l = 0
        for r in range(0, len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res
