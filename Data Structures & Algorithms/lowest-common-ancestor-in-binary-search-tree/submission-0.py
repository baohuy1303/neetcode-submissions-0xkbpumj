# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # break off point is the lowest common ancestor
        if not root:
            return -1
        p_val = p.val
        q_val = q.val
        if root.val > p_val and root.val > q_val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p_val and root.val < q_val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root