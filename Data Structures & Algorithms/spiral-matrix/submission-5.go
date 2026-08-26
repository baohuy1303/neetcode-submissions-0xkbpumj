func spiralOrder(matrix [][]int) []int {
    // stop if top > bottom or right < left

    // top move - col
    // right move - row
    // bottom move - col
    // left move - row

    n := len(matrix)
    m := len(matrix[0])
    left := 0
    right := m - 1
    top := 0
    bottom := n - 1
    res := []int{}

    for{
        for i := left; i <= right; i++{
            res = append(res, matrix[top][i])
        }
        top++

        if top > bottom || left > right{
            return res
        }

        for i := top; i <= bottom; i++{
            res = append(res, matrix[i][right])
        }
        right--

        if top > bottom || left > right{
            return res
        }
        
        for i := right; i >= left; i--{
            res = append(res, matrix[bottom][i])
        }
        bottom--

        if top > bottom || left > right{
            return res
        }

        for i := bottom; i >= top; i--{
            res = append(res, matrix[i][left])
        }
        left++

        if top > bottom || left > right{
            return res
        }
    }
}
