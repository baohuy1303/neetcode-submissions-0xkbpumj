class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        path = []
        # go check if at len then append to res
        # if not then continue going / dfs on the current one
        # decision 1 is to not add the number to path, then send the cur decision down
        # after dfs/decision goes back up, pop then go do the other decision
        def backtrack(i):
            # base case
            if i == n:
                # add a copy because python auto references, which we dont want
                res.append(path[:])  # this creates a snap shot pretty much
                return

            # Not add number in / skip the current number
            backtrack(i+1)

            # Add the number in
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
            return
            

        backtrack(0)
        return res