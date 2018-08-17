'''
@author：KongWeiKun
@file: removeDuplicates.py
@time: 18-3-29 下午8:56
@contact: 836242657@qq.com
'''
"""
Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = 1
        cur_elem = nums[0]
        ind = 1
        for elem in nums[1:]:
            if cur_elem != elem:
                cur_elem = elem
                res += 1
                nums[ind] = elem
                ind += 1
        return res