# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def isSame(node, subNode):
            if node is None and subNode is None:
                return True

            if node is None or subNode is None or node.val != subNode.val:
                return False

            return isSame(node.left, subNode.left) and isSame(node.right, subNode.right)

        def dfs(node, subNode):
            if not node:
                return False
            
            if node.val == subNode.val:
                if isSame(node, subNode):
                    return True
            
            return dfs(node.left, subNode) or dfs(node.right, subNode)
        
        return dfs(root, subRoot)
        