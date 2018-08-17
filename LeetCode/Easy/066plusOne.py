'''
@author：KongWeiKun
@file: 066PlueOne.py
@time: 18-4-26 下午9:02
@contact: kongwiki@163.com
'''
def plusOne(digits):
    """
    
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in range(len(digits)-1,-1,-1):
        digits[i] += carry
        if digits[i] > 9:
            digits[i] -= 10
            carry = 1
        else:
            carry = 0
    if carry > 0:
        digits.insert(0, 1)
    return digits

def plusOne1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        print(digits[i])
        if digits[i] > 9:
            digits[i] -= 10
            carry = 1
        else:
            carry = 0
        if carry == 0:
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

if __name__ == '__main__':
    digits = [1,9,9]
    plusOne1(digits)
    # print(plusOne1(digits))
    # for i in range(len(digits)-1, -1, -1):
    #     digits[i] += 1
    #     print(digits[i])
