"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # clone dictionary
        oldToNew = {}
        # our cloning algorithm
        def dfs(node):
            # if node is in cloned dictionary
            if node in oldToNew:
            # return that value
                return oldToNew[node]
            # create a new node of the current node's value
            copy = Node(node.val)
            # throw that in the new cloned dictionary
            oldToNew[node] = copy
            # scan the neighbors (cloning neighbors section)
            for nei in node.neighbors:
                # copy the neighbors
                copy.neighbors.append(dfs(nei))
            # return the cloned node
            return copy
        # final call to clone all nodes if node isnt null
        return dfs(node) if node else None