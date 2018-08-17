'''
@author  : kongweikun
@file    : 118pascalTriangle.py
@time    : 18-6-28 下午12:50
@contact : kongwiki@163.com
'''
"""
输出杨辉三角
"""

def generate(numRows):
    """
    生成杨辉三角
    :type numRows: 输出行数
    :rtype:
    """
    if not numRows:
        return []
    res = [[1]]
    for i in range(1,numRows):
        res.append([])
        for j in range(i+1):
            res[i].append((res[i - 1][j - 1] if j > 0 else 0) + (res[i - 1][j] if j < i else 0))
    return res

def generate1(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    res = [[1]]
    for i in range(1, numRows):
        print(res[-1]+[0])
        res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
    return res[:numRows]



if __name__ == '__main__':
    a = generate1(5)


