""" number of palindromic substrings
1 <= s.length <= 1000

brute-force: helper palindrome check O(n) -> check at each char with different left and right boundaries
-> O(n^2) * O(n)  -> O(n^3)
abcde

start from the center, spread outwards.
Odd, even palindromes:
Odd:
    - center cur, l = i-1, r = i+1
Even:
    - check both l = i-1, r = i (cur)

O(n^2), for every valid check res += 1
 """

class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        # Odd
        for i in range(n):
            res += 1
            l = i-1
            r = i+1
            while 0 <= l < n and 0 <= r < n:
                if s[l] != s[r]:
                    break
                res += 1
                l -= 1
                r += 1

        # Even
        for i in range(n):
            l = i-1
            r = i
            while 0 <= l < n and 0 <= r < n:
                if s[l] != s[r]:
                    break
                res += 1   
                l -= 1
                r += 1
        
        return res