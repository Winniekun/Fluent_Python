'''
@author  : kongweikun
@file    : 088mergeSortedArray.py
@time    : 18-6-11 下午9:34
@contact : kongwiki@163.com
'''
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""


class Solution:
    @staticmethod
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1Len = len(nums1)
        while nums1Len > m:
            nums1.pop()
            nums1Len -= 1
        nums1.extend(nums2[0:n])
        nums1.sort()
        return nums1

if __name__ == '__main__':
    a = [2,10,4,1,0,0,0,0]
    b = [6,8,6]
    print(Solution.merge(a,4,b,3))

