class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1
        
        res = []
        while True:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
                
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if left > right or top > bottom:
                break
            
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            
            if len(res) == (len(matrix) * len(matrix[0])):
                break
            
        return res