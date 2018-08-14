'''
@author  : kongweikun
@file    : 258addDigits.py
@time    : 18-8-14 下午8:43
@contact : kongwiki@163.com
'''
"""
add digits

example
Input 38
Output 2
"""

def addDigits(num):
    """

    :type num: int
    :type:
    """
    if num == 0:
        return 0
    return 1+(num-1)%9

def addDigits1(num):
    if num <= 9 :
        return num
    while num > 9:
        res = 0
        for digit in num:
            res += int(digit)
        num = res
        

if __name__ == '__main__':
    print(addDigits(38))