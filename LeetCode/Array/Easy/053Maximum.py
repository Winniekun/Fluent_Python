'''
@author：KongWeiKun
@file: 053Maximum.py
@time: 18-4-11 下午8:43
@contact: kongwiki@163.com
'''
'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
def maxSubArray(nums):
    """
    :type nums: list[int] 
    :rtype: int
    """
    if (nums[0] > 0):
        thisSum = nums[0]
    else:
        thisSum = 0
    maxSum = nums[0]

    for num in nums[1:]:
        thisSum += num

        if thisSum > maxSum:
            maxSum = thisSum

        if thisSum < 0:
            thisSum = 0

    return maxSum


def maxSubArray1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # i = 0
    # i_keep = 0
    # j = 1
    # j_keep = 1
    # max_sum = nums[0]-1
    # while j < len(nums) and i < j:
    #     temp_sum = sum(nums[i:j])
    #     if temp_sum >= max_sum:
    #         i_keep = i
    #         j_keep = j
    #         max_sum = temp_sum
    #     elif i == j-1:
    #         i += 1
    #         j += 1
    #     j += 1
    # return max_sum

    # brute force
    # max_sum = nums[0]
    # for i in range(len(nums)):
    #     for j in range(i,len(nums)+1):
    #         temp_sum = sum(nums[i:j])
    #         if temp_sum > max_sum and i != j:
    #             max_sum = temp_sum
    # return max_sum

    # outer loop only
    max_sum = csum = nums[0]
    for num in nums[1:]:
        if num >= csum + num:
            csum = num
        else:
            csum += num

        if csum > max_sum:
            max_sum = csum

    return max_sum

if __name__ == '__main__':
    a = [1]
    s = maxSubArray1(a)
    print(s)