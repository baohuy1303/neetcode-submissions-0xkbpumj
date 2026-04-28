class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # sort, then do the first one, skip the duplicate
        # copy each path iteration to the res
        res = []
        nums.sort()

        def dfs(i, path):
            res.append(path.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                path.append(nums[j])
                dfs(j+1, path)
                path.pop()
            return
        
        dfs(0, [])
        return res