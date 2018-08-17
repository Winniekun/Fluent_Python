'''
@author  : kongweikun
@file    : 058lengthOfLastWord.py
@time    : 18-8-17 下午3:12
@contact : kongwiki@163.com
'''
"""
返回最后一个单词的长度,每个单词以' '隔开

Example:

Input: "Hello World"
Output: 5
"""
import re

def lengthOfLastWord(s):
    pattern = re.compile('[a-zA-Z]+')
    resutl = re.findall(pattern,s)
    if not resutl:
        return 0
    return len(resutl[-1])

if __name__ == '__main__':
    word = "a"
    print(lengthOfLastWord(word))
