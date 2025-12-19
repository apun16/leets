# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """

        """
        reuse function from other lc problem
        """
        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val and
                    isSameTree(p.left, q.left) and
                    isSameTree(p.right, q.right))
        
        if not root:
            return False

        return (isSameTree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))