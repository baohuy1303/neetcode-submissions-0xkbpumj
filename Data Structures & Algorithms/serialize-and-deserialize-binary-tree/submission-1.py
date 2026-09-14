# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = [""]
        def dfs(node):
            if node is None:
                res[0] += ",N"
                return
            res[0] += "," + str(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return res[0]
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def dfs(i):
            if data[i] == "N":
                return None, i
            root = TreeNode(data[i])
            root.left, m = dfs(i+1)
            root.right, n = dfs(m+1)
            return root, n
        return dfs(1)[0]
