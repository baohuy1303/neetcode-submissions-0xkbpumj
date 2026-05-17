class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # go until >= amount
        # at each branch pick cur num or go to next
        # return min out of the 2 branches

        ''' def dfs(i, total, coin_num):
            if i >= len(coins):
                return -1
            if total > amount:
                return -1
            if total == amount:
                return coin_num
            if memo
            keep = dfs(i, total + coins[i], coin_num + 1)
            branch = dfs(i+1, total, coin_num)
            if keep == -1 and branch == -1:
                return -1
            if keep != -1 and branch != -1:
                return min(keep, branch)
            if keep == -1 and branch != -1:
                return branch
            return keep

        return dfs(0, 0, 0) '''
        
        memo = {}
        def dfs(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return -1
            if remain in memo:
                return memo[remain]
            min_coins = float('inf')
            for coin in coins:
                memo[remain-coin] = dfs(remain - coin)
                if memo[remain-coin] != -1:
                    min_coins = min(min_coins, 1 + memo[remain-coin])
                    
            memo[remain] = min_coins
            return memo[remain]
        
        remains = dfs(amount)
        return remains if remains != float('inf') else -1





