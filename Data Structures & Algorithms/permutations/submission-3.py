class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for loop to create new branch at each index
        res = []

        def dfs(tracker, path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i in range(0, len(nums)):
                if tracker[i] == True:
                    continue
                tracker[i] = True
                path.append(nums[i])
                dfs(tracker, path)
                tracker[i] = False
                path.pop()
            return

        dfs([False] * len(nums), [])
        return res
