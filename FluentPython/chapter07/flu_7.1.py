'''
@author  : kongweikun
@file    : flu_7.1.py
@time    : 18-6-24 上午12:09
@contact : kongwiki@163.com
'''
#装饰器的基础知识
def deco(fuc):
    def inner():
        print("running inner()")
    return inner

@deco
def target():
    print("runing target()")

if __name__ == '__main__':
    target()