'''
@author  : kongweikun
@file    : 011containerWithMostWater.py
@time    : 18-8-17 下午7:23
@contact : kongwiki@163.com
'''

def maxArea(height):
    """
    :type height:
    :rtype:
    """
    ans = 0
    l = 0
    r = len(height) - 1
    while l < r:
        ans = max(ans,(r-l)*min(height[l],height[r]))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans

if __name__ == '__main__':
    a = [1,2,1]
    ans = maxArea(a)
    print(ans)