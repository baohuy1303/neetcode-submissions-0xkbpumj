# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, smallest, largest):
            if node is None:
                return True
            if node.val >= largest or node.val <= smallest:
                return False
            
            
            left = dfs(node.left, smallest, node.val)
            right = dfs(node.right, node.val, largest)

            return (left and right)
        
        return dfs(root, -float('inf'), float('inf'))