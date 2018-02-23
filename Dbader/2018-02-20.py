'''
@author：KongWeiKun
@file: 2018-02-20.py
@time: 18-2-20 下午4:08
@contact: 836242657@qq.com
'''
a = [1,2,3]
b = a
print(a is b)

c = list(a)
print(a == c)
print(a is c)