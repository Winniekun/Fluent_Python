'''
@author  : kongweikun
@file    : 004medianOfTwoSortedArrays.py
@time    : 18-8-17 下午8:59
@contact : kongwiki@163.com
'''
"""
求两个数组排序之后的中值
Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

def findMedianSortedArrays(nums1,nums2):
    nums1.extend(nums2)
    nums1 = sorted(nums1)
    if len(nums1)%2 == 1:
        return nums1[len(nums1)//2]/1
    else:
        return (nums1[len(nums1)//2]+ nums1[len(nums1)//2 - 1])/2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    s = findMedianSortedArrays(nums1,nums2)
    print(s)