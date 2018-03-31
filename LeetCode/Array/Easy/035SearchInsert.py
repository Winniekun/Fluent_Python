'''
@author：KongWeiKun
@file: 35SearchInsert.py
@time: 18-3-31 下午8:41
@contact: kongwiki@163.com
'''
import time

'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low+high)//2
        guess = nums[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return low

def  searchInsert1(nums,target):
    num = [i for i in nums if i <target]
    return len(num)

if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 2
    start = time.time()
    print(searchInsert(nums,target))
    print(searchInsert1(nums,target))



