func maxSubArray(nums []int) int {
    cur_sum := nums[0]
    res := cur_sum
    for i := 1; i < len(nums); i++ {
        num := nums[i]
        if cur_sum + num < num{
            cur_sum = num;
        }else{
            cur_sum += num;
        }
        res = max(res, cur_sum)
    }
    return res
}
