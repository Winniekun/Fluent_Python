'''
@author  : kongweikun
@file    : 021mergeTwoSortedLists.py
@time    : 18-8-15 下午12:43
@contact : kongwiki@163.com
'''
import re
def mergeTwoLists(l1,l2):
    """
    :type l1:
    :type l2:
    :type:
    """
    for i in l2:
        l1.append(i)
    l1 = sorted(l1)
    print(l1)

if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    mergeTwoLists(l1,l2)