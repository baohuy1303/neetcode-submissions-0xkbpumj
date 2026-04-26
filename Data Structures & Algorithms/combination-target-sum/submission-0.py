class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ''' 
        each layer, consider an index
        but this may introduce duplicates. so we will choose either to include
        this current path OR not at all.
        For ex: 
            [2]         []
        [2,2] [2]    [3]    []....

        impossible to reach target cases:
        + index > len(nums)
        + cur_sum > target

        base case:
        cur_sum == target
        '''

        res = []

        def dfs(index, cur_path, cur_sum):
            # base
            if cur_sum == target:
                res.append(cur_path.copy())
                return
            
            if index > len(nums) - 1 or cur_sum > target:
                return

            cur_num = nums[index]
            cur_path.append(cur_num)
            
            # include cur combination
            dfs(index, cur_path, cur_sum + cur_num)
            cur_path.pop()

            # never include the combination
            dfs(index + 1, cur_path, cur_sum)

        dfs(0, [], 0)

        return res

            

            


