''' ALL POSSIBLE subsets

at each number, we gonna decide to include or exclude to cur path.
we just keep going until we reach the end/len(nums) and we append that to our res

NO DUPLICATES tho?

sort. DFS: For each number, we'll loop j from i+1 til end
we'll try going down the path including and excluding j

we'll have a main for loop that skips over duplicated number

 '''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, path):
            if i >= len(nums):
                res.append(path)
                return

            path.append(nums[i])
            dfs(i+1, path.copy())
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            
            dfs(i+1, path.copy())
        dfs(0, [])
        return res


