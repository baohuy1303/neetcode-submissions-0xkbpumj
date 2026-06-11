''' go from n - 1 -> 0
add 1 to n-1
if >= 10, then we remember it

at the end, if there is still a remember, we add 1 to the front
 '''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 0
        digits[-1] += 1
        if digits[-1] >= 10:
            digits[-1] = 0
            rem = 1
        for i in range(len(digits) - 2, -1, -1):
            digits[i] += rem
            rem = 0
            if digits[i] >= 10:
                digits[i] = 0
                rem = 1
        if rem == 1:
            return [1] + digits
        return digits
            