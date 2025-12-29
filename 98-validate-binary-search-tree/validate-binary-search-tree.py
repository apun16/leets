class Solution(object):
    def isValidBST(self, root):
        self.prev = None
        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if self.prev is not None and node.val <= self.prev:
                return False
            self.prev = node.val
            return dfs(node.right)
        return dfs(root)