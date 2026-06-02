class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]

            res = float('inf')
            for coin in coins:
                res = min(1 + dfs(amount - coin), res)
            memo[amount] = res
            return res
        res = dfs(amount)
        if res == float('inf'):
            return -1
        return res