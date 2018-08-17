'''
@author  : kongweikun
@file    : 717.1-bitand2-bitCharacters.py
@time    : 18-7-16 下午3:48
@contact : kongwiki@163.com
'''
"""
example 
bits = [1,0,0]
Output: True
Expanation:
The only way to decode it is two-bit character and one-bit character.
So the charaacter is one-bit character.
即判断给出的数组最后一个元素是属于 ‘0’ 还是 ‘10’，若是‘0’则返回True 若是‘10’
则返回False
"""

def isOneBittCharacter(bits):
    """
    判断最后一个元素0 属于哪一个内容
    :type bits:
    :rtype:
    """
    if not bits:
        return False
    count = 0
    while count < len(bits)-1:
        if bits[count] == 0:
            count += 1
        else:
            count += 2

    if count == len(bits)-1:
        return True
    else:
        return False


"""
最优解
"""
def isOneBitCharacter(bits):
    index, n = 0, len(bits)
    while index < n:
        if index == n-1: return True
        if bits[index] == 0:
            index += 1
        else: index += 2
    return False

if __name__ == '__main__':
    a = [1,0,0]
    print(isOneBittCharacter(a))