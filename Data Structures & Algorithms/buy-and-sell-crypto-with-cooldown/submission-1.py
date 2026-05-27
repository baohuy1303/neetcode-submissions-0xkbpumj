class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, not buy, sell (if have enough)
        # if bought, cannot buy until sell
        # if sell, needs to wait for 1 day (i + 2)

        # at each index, decide if buy or not buy (1)
        # if not buy, i+1 then repeat (1)
        # if buy, then decide when to sell (flag it down the path?)
        # at each index decide whether to sell or not to sell
        # if sold, i+2 and repeat (1)
        memo = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            res = 0
            if (i, buying) in memo:
                return memo[(i,buying)]

            if buying:
                buy = -prices[i] + dfs(i+1, False)
                not_buy = dfs(i+1, True)
                res += max(buy, not_buy)
            else:
                sell = prices[i] + dfs(i+2, True)
                not_sell = dfs(i+1, False)
                res += max(sell, not_sell)
            memo[(i, buying)] = res
            return res
        
        return dfs(0, True)