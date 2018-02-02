'''
@author：KongWeiKun
@file: longest_non_repeat.py
@time: 18-1-31 下午3:26
@contact: 836242657@qq.com
'''
'''
给定一个字符串，找到最长的子字符串的长度不重复字符。
例子：
给定“abcabcbb”，答案是“abc”，长度是3。
给定“bbbbb”，答案是“b”，长度为1。
给定“pwwkew”，答案是“wke”，长度为3。
请注意，答案必须是一个子字符串，
“pwke”是一个子序列，而不是一个子字符串。
'''
"""
例如：一个字符串   awbcdewgh
他的子串：  awbc.   awbcd   awbcde   ....很多个子串  但是都是连续在一起  
他的子序列： abc  .  abcd    abcde  ...  很多个子序列  
但是子序列中的字符在字符串中不一定是连在一起的， 
但是  子序列一定是单调的， （即字符之间ASCII单调递增或单调递减）
"""

def longest_non_repeat(s):
    start, maxlen = 0, 0
    used_char = {}
    for i, char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen, i-start+1)

        used_char[char] = i
    return maxlen



def longest_non_repeats(s):
    start , maxlen = 0 , 0
    used_char = {}
    for i ,char in enumerate(s):
        if char in used_char and start <= used_char[char]:
            start = used_char[char] + 1
        else:
            maxlen = max(maxlen,i-start+1)
        used_char[char] = i

    return maxlen

a = "abcabcdefbb"
print(longest_non_repeats(a))