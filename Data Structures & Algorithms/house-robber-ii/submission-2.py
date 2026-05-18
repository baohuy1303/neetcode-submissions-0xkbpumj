class Solution:
    def rob(self, nums: List[int]) -> int:
        # only check if first num in arr and last num in arr

        arr_1 = []
        arr_2 = []
        for i in range(len(nums)):
            if i == 0:
                arr_1.append(nums[i])
                continue
            if i == len(nums) - 1:
                arr_2.append(nums[i])
                continue
            arr_1.append(nums[i])
            arr_2.append(nums[i])

        memo1 = {}
        memo2 = {}

        def dfs_1(i):
            if i >= len(arr_1):
                return 0
            if i in memo1:
                return memo1[i]
            memo1[i] = max(dfs_1(i+1), arr_1[i] + dfs_1(i+2))
            return memo1[i]


        def dfs_2(i):
            if i >= len(arr_2):
                return 0
            if i in memo2:
                return memo2[i]
            memo2[i] = max(dfs_2(i+1), arr_2[i] + dfs_2(i+2))
            return memo2[i]

        return max(dfs_1(0), dfs_2(0))