func maxProfit(prices []int) int {
// buy lowest sell highest
    // buy date < sell date

    // keep track of lowest buy up until ith day
    // keep max cur_profit = cur_sell - lowest_buy

    res := 0
    lowest_buy := prices[0]

    for i := 1; i < len(prices); i++{
        if prices[i] - lowest_buy > res{
            res = prices[i] - lowest_buy
        }
        if prices[i] < lowest_buy{
            lowest_buy = prices[i]
        }
    }

    return res
}
