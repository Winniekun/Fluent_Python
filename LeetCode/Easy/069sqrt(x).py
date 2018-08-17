'''
@author  : kongweikun
@file    : 069sqrt(x).py
@time    : 18-8-17 下午3:24
@contact : kongwiki@163.com
'''
"""
求数字的根
Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

def mySqrt(x):
    for i in range(x//2):
        if i**2 == x:
            return i
        elif i**2 < x < (i+1)**2:
            return i
if __name__ == '__main__':
    x = 4
    assert mySqrt(8) == 2