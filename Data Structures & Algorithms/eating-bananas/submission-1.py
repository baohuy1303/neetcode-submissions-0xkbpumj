class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            res = 0
            for p in piles:
                if k > p:
                    res += 1
                    continue
                res += math.ceil(p / k)
            return res

        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (r + l) // 2
            if check(m) <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        
            