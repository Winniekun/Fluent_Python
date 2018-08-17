'''
@author  : kongweikun
@file    : 028implementStrStr().py
@time    : 18-8-15 下午1:18
@contact : kongwiki@163.com
'''
"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

def strStr(haystack, needle):
    m = len(haystack)
    n = len(needle)
    # 'cat' ''
    if n == 0:
        return 0
    if m < n:
        return -1

    for i in range(m-n+1):
        for j in range(n):
            if haystack[i+j]!= needle[j]:
                break
            else:
                if j == n -1:
                    return i
    return -1

if __name__ == '__main__':
    haystack = "aa"
    needle = "aaa"
    print(strStr(haystack,needle))