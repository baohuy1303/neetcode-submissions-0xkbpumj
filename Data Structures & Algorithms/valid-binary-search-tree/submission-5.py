# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, min_range, max_range):
            if node is None:
                return True

            if min_range >= node.val or max_range <= node.val:
                return False

            if not dfs(node.left, min_range, min(node.val, max_range)):
                return False
            
            if not dfs(node.right, max(node.val, min_range), max_range):
                return False

            return True

        return dfs(root, -float('inf'), float('inf'))