# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

''' know where the kth element is:
    - before traversing:
        - 
    - after traversing all:
        - still need to iterate the result after traversing to find kth element
        - get size and go to kth element? ONlogk?
 '''
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = [0]
        res = [0]

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            counter[0] += 1
            if counter[0] == k:
                res[0] = node.val
            dfs(node.right)
            
            return
            
        dfs(root)
        return res[0]
