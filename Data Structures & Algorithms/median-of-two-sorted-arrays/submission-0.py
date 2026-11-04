class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        l = 0
        r = len(A) - 1
        while True:
            A_mid_i = (r+l) // 2
            B_mid_i = half - A_mid_i - 2

            A_left = A[A_mid_i] if A_mid_i >= 0 else -float('inf')
            A_right = A[A_mid_i + 1] if A_mid_i + 1 < len(A) else float('inf')
            B_left = B[B_mid_i] if B_mid_i >= 0 else -float('inf')
            B_right = B[B_mid_i + 1] if B_mid_i + 1 < len(B) else float('inf')
            
            if A_left <= B_right and A_right >= B_left:
                if total % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return min(A_right, B_right)

            elif A_left > B_right:
                r = A_mid_i - 1
            else:
                l = A_mid_i + 1
            
        return