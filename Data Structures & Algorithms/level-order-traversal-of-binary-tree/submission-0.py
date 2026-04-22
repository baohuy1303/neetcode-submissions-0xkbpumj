# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # marking them in some way?
        if root is None:
            return []

        q = deque()
        q.append((root, 0))
        res = []
        while q:
            cur_tuple = q.popleft()
            cur_node = cur_tuple[0]
            cur_level = cur_tuple[1]
            if len(res) < cur_level + 1:
                res.append([])
            res[cur_level].append(cur_node.val)
            if cur_node.left:
                q.append((cur_node.left, cur_level + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_level + 1))
        return res
            
