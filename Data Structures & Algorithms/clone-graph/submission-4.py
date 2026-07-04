"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
""" copy the same values and structure, but fundamentally a different object 
node val = node index
adj_list graph

return 1st node of copied graph

connected undirected graph -> dfs will be enough

DFS and create nodes with hashmap: value/index -> address of the node
Continue traversing the orginal graph to build up the relationship of the nodes
O(n)
always be the first node with val = 1.
 """

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_lookup = {} # value/index: address

        def dfs(n):
            if n is None:
                return

            new_node = Node(n.val)
            node_lookup[new_node.val] = new_node
            new_neighbors = []
            for neighbor in n.neighbors:
                if neighbor.val in node_lookup:
                    new_neighbors.append(node_lookup[neighbor.val])
                    continue

                dfs(neighbor)
                new_neighbors.append(node_lookup[neighbor.val])

            new_node.neighbors = new_neighbors
            return
        
        dfs(node)
        if len(node_lookup) == 0:
            return None
        return node_lookup[1]