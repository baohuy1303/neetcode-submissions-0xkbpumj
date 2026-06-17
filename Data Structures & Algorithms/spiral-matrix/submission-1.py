''' keep track of boundaries

-> top row
|| rightmost column
<- bottom row
|| leftmost column

-> top row + 1
|| rightmost - 1
<- bottom -1
|| left most + 1

keep track of each layers max
go each dir until reach max of the next layer, increament current layer and go

O(1) extra space so no seen set

when do we stop?
    - the 4 vars === to each other? we keep a record of the last layers result.
    if after the 4 dirs and its still the same then we can stop?
 '''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        left = 0

        res = []
        while True:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1

            if len(res) == (len(matrix) * len(matrix[0])):
                break

            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1

            if len(res) == (len(matrix) * len(matrix[0])):
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1

            if len(res) == (len(matrix) * len(matrix[0])):
                break

            for i in range(bottom, top-1, -1):
                res.append(matrix[i][left])
            left += 1

            if len(res) == (len(matrix) * len(matrix[0])):
                break

        return res 
        