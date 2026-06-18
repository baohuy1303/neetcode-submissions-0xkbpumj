''' always a square
90 deg clockwise

brute-force (store new array):
    - we would reverse row and col on the res array
    (org[r][2] -> res[2][len(n) - 1 - r])

cant store a row or col

rotate in-place?
    - transpose and then flip
 '''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        # transpose (only want elements upper triangle, above the nega diagonal / main digonal line)
        # because if we go thru the elements below it again, its flipped again
        # flip 2 times = same place
        # so we j to always be larger than i (to only go over upper triangle)
        
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # flip from vertical middle
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]
