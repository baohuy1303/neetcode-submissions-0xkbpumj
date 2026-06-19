''' subarray that has the largest product
return the product

brute-force: O(n^2)

if we skip for min and max, then we take the cur one (subarray no holes)
 '''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        min_prod, max_prod = 1, 1
        res = nums[0]
        for num in nums:
            min_prod, max_prod = min(num, num*min_prod, num*max_prod), max(num, num*max_prod, num*min_prod)
            res = max(max_prod, res)
        return res
        
        