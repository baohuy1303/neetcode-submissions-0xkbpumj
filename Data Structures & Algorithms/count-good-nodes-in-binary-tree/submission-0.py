# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of cur_max from root
        # update cur_max down the path
        # if value > cur_max then it's a good node, then update cur_max
        # dfs
        if root is None:
            return 0

        res = 0
        cur_max = root.val

        def dfs(node, cur_max):
            if node is None:
                return 0

            count = 0
            if node.val >= cur_max:
                count = 1
                cur_max = node.val
    
            # Sum up the results from children
            return count + dfs(node.left, cur_max) + dfs(node.right, cur_max)
        
        return dfs(root, root.val)

        