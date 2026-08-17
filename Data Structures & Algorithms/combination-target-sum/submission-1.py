class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur_sum, path):
            if i >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i, cur_sum + nums[i], path)
            path.pop()
            dfs(i+1, cur_sum, path)

        dfs(0, 0, [])
        return res