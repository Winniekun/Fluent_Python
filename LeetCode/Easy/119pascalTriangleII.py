'''
@author  : kongweikun
@file    : 119pascalTriangleII.py
@time    : 18-6-29 下午11:15
@contact : kongwiki@163.com
'''
"""
帕斯卡三角二
"""
def getRow(rowIndex):
    """
    帕斯卡三角，返回改行的元素
    :type rowIndex: 第几行
    :rtype:
    """
    res = [[1]]
    for i in range(0,rowIndex):
        if rowIndex == 0:
            return res
        res.append(list(map(lambda x, y : x + y, res[-1] + [0], [0] + res[-1])))
    return res[rowIndex]

def getRow1(rowIndex):
    res = [1]
    cur = rowIndex
    for i in range(rowIndex//2):
        res += res[-1]*cur//(i+1),
        cur -= 1
    if rowIndex % 2 == 0:
        res = res + res[:-1][::-1]
    else:
        res = res[::-1]
    return res

if __name__ == '__main__':
    # print(getRow(3))
    # print(4/2)
    print(getRow1(4))
