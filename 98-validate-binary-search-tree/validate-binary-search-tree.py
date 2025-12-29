class Solution(object):
    def isValidBST(self, root):
        def inorder(node, prev=[float('-inf')]):
            if not node: return True
            if not inorder(node.left, prev): return False
            if node.val <= prev[0]: return False
            prev[0] = node.val
            return inorder(node.right, prev)
        return inorder(root)