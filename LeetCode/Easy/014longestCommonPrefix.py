'''
@author  : kongweikun
@file    : 014longestCommonPrefix.py
@time    : 18-8-13 下午11:10
@contact : kongwiki@163.com
'''
"""

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

def longestCommonPrefix(strs):
    """
    :type strs:
    :rtype:
    """
    if not strs or len(strs) == 0:
        return ""
    prefix = strs[0]
    for i in range(1,len(strs)):
        j = 0
        while j < min(len(strs[i]), len(prefix)):
            if strs[i][j] != prefix[j]:
                break
            j += 1
        prefix = prefix[:j]
    return prefix


def longestCommonPrefix1(strs):
    prefix = []
    for chars in zip(*strs):
        charset = set(chars)
        if len(charset) == 1:
            prefix.append(charset.pop())
        else:
            break

    return "".join(prefix)

def longestCommonPrefix2(strs):
    if not strs:
        return ""
    for i, ch in enumerate(zip(*strs)):
        if len(set(ch)) != 1:
            return strs[0][:i]
    else:
        return min(strs, key=len)

if __name__ == '__main__':
    s = ["flower","flow","flight"]
    for i ,ch in enumerate(zip(*s)):
        print(set(ch))
    # a = longestCommonPrefix(s)
    # print(a)