'''
@author  : kongweikun
@file    : 020validParentheses.py
@time    : 18-8-14 下午11:01
@contact : kongwiki@163.com
'''
"""
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

def isValid(s):
    """
    :type s:
    :rtype:
    """
    if len(s) % 2 == 1:
        return "false"
    stack = []
    left = ('{','[','(')
    right = ('}',']',')')
    zip(left,right)
    for vec in s:
        if vec in left:
            stack.append(vec)
        else:
            if not stack:
                return 'false'
            p = stack.pop()
    return len(stack) == 0


def isValid1(s):
    RULE = ['{','[','(']
    MAP = {"]": "[", "}": "{", ")": "("}
    stack = []
    for single in s:
        if single in RULE:
            stack.append(single)
        elif not stack:
            return 'false'
        elif stack.pop() != MAP[single]:
            return 'false'
    return not stack


if __name__ == '__main__':
    s = "(){}[]"
    print(isValid1(s))
