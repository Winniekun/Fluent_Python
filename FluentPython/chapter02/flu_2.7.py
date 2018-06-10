'''
@author  : kongweikun
@file    : flu_2.7.py
@time    : 18-6-10 下午11:11
@contact : kongwiki@163.com
'''
"""
list.sort方法和内置函数sorted
"""
fruits = ['grape','raspberry','apple','banana']
print(sorted(fruits))
print(sorted(fruits,key=len))
print(sorted(fruits,key=len,reverse=True))
print(fruits.sort())
print(fruits)
