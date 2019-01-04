''' 
@author: weikunkun
@file:   101symmetricTree.py
@time:   19-1-3上午11:13
@contact: kongwiki@163.com
'''


'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center)

判断二叉树是否对称
'''

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self._isSymmetric(root.left, root.right)

    def _isSymmetric(self, left, right):
        """
        :param left:
        :param right:
        :return:
        """
        if not right or not left:
            return False
        if not right and not left:
            return True

        if right.val != left.val:
            return False
        return self._isSymmetric(left.left, right.right) and self._isSymmetric(left.right, right.left)


    def isSymmetric_iterate(self,root):
        """
        非递归
        :param root:
        :return:
        """
        if not root:
            return True
        stack1, stack2 = [], []
        stack1.append(root.left)
        stack2.append(root.right)
        if len(stack1) != len(stack2):
            return False

        while stack2 and stack1:
            len1 = len(stack1)
            len2 = len(stack2)

            if len1 != len2:
                return False
            for _ in range(len2):
                curr1, curr2 = stack1.pop(), stack2.pop()
                if not curr1 and not curr2:
                    continue
                if not curr1 or not curr2:
                    return False
                if curr1.val != curr2.val:
                    return False
                stack1.append(curr1.left)
                stack1.append(curr1.right)
                stack2.append(curr2.right)
                stack2.append(curr2.left)
        return not stack1 and not stack2

