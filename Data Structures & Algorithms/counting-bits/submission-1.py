class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n+1)
        for i in range(0, n+1):
            num = i
            while num:
                res[i] += num & 1
                num = num >> 1
        return res