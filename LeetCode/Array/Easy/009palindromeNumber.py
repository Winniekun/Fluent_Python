'''
@author  : kongweikun
@file    : 009palindromeNumber.py
@time    : 18-8-4 上午9:25
@contact : kongwiki@163.com
'''
"""
回文数字

input 121
Output true

input -121
Output false

Input 10
Output false
"""
def isPalindrome(x):
    """

    :type x:
    :rtype:
    """
    b = "".join(list(reversed(str(x))))
    if str(a) == b:
        return True
    else:return False

def isPalindrome2(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False

def isPalindrome1(self, x):
    """
    :type x: int
    :rtype: bool
    """
    str_value = str(x)
    if str_value == str_value[::-1]:
        return True
    else:
        return False


if __name__ == '__main__':
    a = 121
