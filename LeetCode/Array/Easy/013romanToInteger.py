'''
@author  : kongweikun
@file    : 013romanToInteger.py
@time    : 18-8-12 下午8:29
@contact : kongwiki@163.com
'''
"""
Roman numerals are represented by seven different symbols: 
I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""
def romanToInt(s):
    romanDic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = romanDic[s[-1]]
    for i in range(len(s) - 2, -1 , -1):
        if romanDic[s[i]] >= romanDic[s[i+1]]:
            result += romanDic[s[i]]
        else:
            result -= romanDic[s[i]]
    return result

if __name__ == '__main__':
    s = 'VII'
    print(romanToInt(s))
    # print(len(s))