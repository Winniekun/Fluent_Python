'''
@author：KongWeiKun
@file: kwargs_learn.py
@time: 18-2-20 下午3:21
@contact: 836242657@qq.com
'''
"""
**kwargs 允许你将不定长度的键值对, 作为参数传递给一个函数。 
如果你想要在一个函数里处理带名字的参数, 你应该使用**kwargs。
"""
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

greet_me(name='yasoob')