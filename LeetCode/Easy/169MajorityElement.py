'''
@author  : kongweikun
@file    : 169MajorityElement.py
@time    : 18-7-20 下午6:19
@contact : kongwiki@163.com
'''

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    result = sorted(counts.items(),key=lambda x: x[1],reverse=True)
    return result[0][0]


def majorityElement1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    print(nums)
    print(len(nums)//2)
    print(nums[len(nums)//2])
    return nums[len(nums) // 2]

if __name__ == '__main__':
    a = [1,2,3,4,56,1,2,1]
    s = majorityElement1(a)
    print(s)