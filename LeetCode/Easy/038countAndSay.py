'''
@author  : kongweikun
@file    : 038countAndSay.py
@time    : 18-8-17 下午2:22
@contact : kongwiki@163.com
'''
"""
1
11
21
1211
111221
312211
用数字读出上一个输入的数字
如 第二行意思是 第一行为1个1

第一行
Example 1:
Input: 1
Output: "1"

第四行
Example 2:
Input: 4
Output: "1211"
"""
def countAndSay(n):
    """
    :type n:
    :rtype:
    """
    oldResult = '1'
    for i in range(n -1 ):
        tmp = ''
        count = 1
        for j in range(1,len(oldResult)+1):
            if j < len(oldResult) and oldResult[j] == oldResult[j-1]:
                count += 1
            else:
                tmp += str(count) + oldResult[j-1]
                count = 1

        oldResult = tmp
    return oldResult





if __name__ == '__main__':
    n = 3
    print(countAndSay(n))