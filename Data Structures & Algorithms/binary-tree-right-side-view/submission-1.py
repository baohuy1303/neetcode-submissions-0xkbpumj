# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # always right first
        # if node.right empty only then start going left
        # any node needs to be verified with the last appened res node, to see if
        # they are levels lower?
        # track stack = [ node ]
        # hash: key - node : val - level?
        if root is None:
            return []
            
        track = []
        level_dict = {}
        current_level = 0
        track.append(root)
        level_dict[root] = current_level

        def addRightSide(node, track, current_level, level_dict):
            print(node.val, current_level)

            if level_dict[track[-1]] < current_level:
                track.append(node)
                level_dict[node] = current_level
            if node.right:
                addRightSide(node.right, track, current_level + 1, level_dict)
            if node.left:
                addRightSide(node.left, track, current_level + 1, level_dict)
        
        if root.right:
            addRightSide(root.right, track, current_level + 1, level_dict)
        if root.left:
            addRightSide(root.left, track, current_level + 1, level_dict)
        
        res = []
        for node in track:
            res.append(node.val)

        return res


        

            

