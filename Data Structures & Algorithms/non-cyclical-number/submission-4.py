class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        res = n
        while res != 1:
            new_num = 0
            while n > 0:
                new_num += (n%10)**2
                n = n // 10
            if new_num in seen:
                return False
            seen.add(new_num)
            n = new_num
            res = new_num
        return True