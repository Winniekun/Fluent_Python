'''
@author  : kongweikun
@file    : 167TwoSumII.py
@time    : 18-7-20 下午5:53
@contact : kongwiki@163.com
'''
"""
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    dic = {}
    for index, number in enumerate(numbers):
        if number in dic:
            return [dic[number],index]
        dic[target-number] = index

def twoSum1( numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    seen = {numbers[0]: 0}
    for i in range(1, len(numbers)):
        if (target - numbers[i]) in seen:
            return [seen[(target - numbers[i])] + 1, i + 1]
        seen[numbers[i]] = i