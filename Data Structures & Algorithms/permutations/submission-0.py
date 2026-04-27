class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # for loop to create new branch at each index
        res = []

        def dfs(index, tracker, path):
            print(path.copy())
            if len(path) == len(nums):
                res.append(path.copy())
                return

            if index >= len(nums):
                return

            
            for i in range(0, len(nums)):
                if tracker[i] == True:
                    continue
                tracker[i] = True
                path.append(nums[i])
                dfs(i, tracker, path)
                tracker[i] = False
                path.pop()
            return

        dfs(0, [False] * len(nums), [])
        return res
