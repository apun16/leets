"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        if not node:
            return None

        cloned = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for nei in curr.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    queue.append(nei)
                cloned[curr].neighbors.append(cloned[nei])

        return cloned[node]