class Solution:
    def reverseBits(self, n: int) -> int:
        cur_power = 31
        res = 0
        while n != 0:
            if bin(n)[-1] == '1':
                res += 2**cur_power
            cur_power -= 1
            n = n >> 1
        return res