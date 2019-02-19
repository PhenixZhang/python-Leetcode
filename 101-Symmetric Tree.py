'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.symmetric(root.left,root.right)
    def symmetric(self,l1,l2):
        if not l1 or not l2:
            if not l1 and not l2:
                return True
            else:
                return False
        if l1.val == l2.val:
            return self.symmetric(l1.left,l2.right) and self.symmetric(l1.right,l2.left)
        else:
            return False
