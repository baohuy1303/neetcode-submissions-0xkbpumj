""" helper palindrome func O(n) to check
check from each letter and the end, only use helper if start match end -> O(n^3)

-> 1000 so O(n^2) should work?

From each letter, we treat it as the center of a palindrome
Spread out on each side, if valid then continue.
Do this for each letter -> O(n^2)

Edge: Odd palindrome, even palindrome
- Odd: pick current letter and expand -1, +1
- Even: try to match with the letter before, if matches then spread from before and cur

Odd:
- For loop from each letter, while loop to expand inside (check bounds)
- If valid and matches, then +2 and continue expanding.
- If not valid or doesnt match, update max_res
 """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        best_l = 0
        best_r = 0
        n = len(s)

        # Odd
        for i in range(n):
            cur_len = 1
            l = i - 1
            r = i + 1

            while 0 <= l < n and 0 <= r < n:
                if s[l] != s[r]:
                    break
                cur_len += 2
                l -= 1
                r += 1
            if cur_len > max_len:
                best_l = l+1
                best_r = r
                max_len = cur_len
        
        # Even
        for i in range(n):
            cur_len = 0
            l = i - 1
            r = i

            while 0 <= l < n and 0 <= r < n:
                if s[l] != s[r]:
                    break
                cur_len += 2
                l -= 1
                r += 1
            if cur_len > max_len:
                best_l = l+1
                best_r = r
                max_len = cur_len

        return s[best_l:best_r]
        