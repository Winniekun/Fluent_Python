'''
@author  : kongweikun
@file    : 100sameTree.py
@time    : 18-8-26 下午9:32
@contact : kongwiki@163.com
'''

class TreeNode(object):

    def __init__(self):
        self.lchild = None
        self.rchild = None
        self.val = None


class Solution(object):

    def isSameTree(self,p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and  not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.lchild, q.lchild) and self.isSameTree(p.rchild, q.rchild)
        return False

