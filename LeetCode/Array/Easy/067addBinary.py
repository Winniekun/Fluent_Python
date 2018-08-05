'''
@author  : kongweikun
@file    : 067addBinary.py
@time    : 18-7-29 下午8:27
@contact : kongwiki@163.com
'''
"""
input a = '11' b = '1'
output  '100'

input a = '1010' b = '1011'
output  '10101'
"""
def addBinary(a,b):
    """
    :type a:
    :type b:
    :type:
    """
    result = []
    carry = val = 0
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(a)):
        val = carry
        val += int(a[-(i+1)])
        if i < len(b):
            val += int(b[-(i+1)])
        carry, val = val//2, val%2
        result.append(str(val))
    if carry :
        result.append(str(carry))
    return "".join(result[::-1])

def addBinary1(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = []
    val = plus = 0
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(a)):
        val = plus
        val += int(a[-(i+1)])
        if i < len(b):
             val += int(b[-(i+1)])
        val,plus = val % 2, val // 2
        res.append(str(val))
    print(plus)
    if plus:
        res.append(str(plus))
    return "".join(res[::-1])

def addBinary2(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

if __name__ == '__main__':
    a = '11'
    b= '1'
    print(addBinary2(a,b))
    # for i in range(10,0,-1):
    #     print(i)
    print(int(a,2)+int(b,2))
    print(bin(4))
    print(bin(11+1))