# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def mirror(a, b):
            if not a or not b:
                return a is b
            return (a.val == b.val and
                    mirror(a.left, b.right) and
                    mirror(a.right, b.left))

        return mirror(root.left, root.right) if root else True