class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(i, total):
            if i >= len(coins) or total > amount:
                return float('inf')

            if total == amount:
                return 0

            if (i, total) in memo:
                return memo[(i, total)]
            memo[(i, total)] = min(1 + recurse(i, total + coins[i]), recurse(i+1, total))
            return memo[(i, total)]

        res = recurse(0, 0)

        return res if res != float('inf') else -1