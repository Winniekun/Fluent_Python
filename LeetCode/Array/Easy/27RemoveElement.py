'''
@author：KongWeiKun
@file: 27RemoveElement.py
@time: 18-3-29 下午8:58
@contact: 836242657@qq.com
'''
"""
Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.
"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    for i in range(nums.count(val)):
        nums.remove(val)
    print(nums)
    return len(nums)

if __name__ == '__main__':
    nums = [1,2,3,4,4,6]
    val = 6
    a = nums.count(4)
    print(a)
    s = removeElement(nums=nums,val=val)
    print(s)
