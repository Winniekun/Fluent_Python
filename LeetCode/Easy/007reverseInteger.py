'''
@author  : kongweikun
@file    : 007reverseInteger.py
@time    : 18-7-26 下午5:44
@contact : kongwiki@163.com
'''
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
"""

def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    x_max = 2**31-1
    x_min = -2**31
    if x < 0:
        result = -1*int(str(abs(x))[::-1])
    else:
        result = int(str(x)[::-1])

    if result > x_max or result<x_min:
        return 0
    return result

if __name__ == '__main__':
    print(reverse(-2147483648))