"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # create new nodes if not created.
        # if created keep a dict and point towards that node based on val

        if not node:
            return None
        
        seen = {}

        def clone(node):
            root = Node(node.val, [])
            seen[node] = root
            for neighbor in node.neighbors:
                if neighbor not in seen:
                    new_node = clone(neighbor)
                    root.neighbors.append(new_node)
                else:
                    root.neighbors.append(seen[neighbor])
            return root

        return clone(node)
        

