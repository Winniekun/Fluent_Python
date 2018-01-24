Fluent Pythoh 
Effective Python
以及一些Python的基础知识学习

--------------------------------------------------------
Fluent Python 更新到2.7   ----2017/12/16
添加经典算法(冒泡排序)的python实现   ----2018/1/2
添加经典算法(冒泡排序优化)的python实现  ----2018/1/3
添加一些不仔细注意且易错的Python语法问题  ----2018/1/21
例子：
#1
#a)eval b)assert c)nonlocal d)pass 哪个不是python3中的关键字

#2
3*1**3值为多少

#3
#下列两个表达式的输出内容是什么
a = 1
b = 1
#a is b 结果为？
print(a is b)
a = 998
b = 998
#a is b 结果为？
print(a is b )
print('\n')
#4
#下面函数的返回只是什么
def func(a):
    a = a + '2'
    a = a*2
    return a
print(func('hello'))

#5
#在python中 表达式 0.1+0.2==0.3 的返回是
print(0.1+0.2)

#6
#表达式~~~5的值是多少
print(~~~5)
#-6

#7
#表达式bool('False')的返回值
print(bool('False'))

#8
#表达式True==False==False的值
print(True==False==False)

#9
#下面表达式的输出结果为
i = 0
while i < 5:
    print(i)
    i +=1
    if i ==3:
        break
else:
    print(0)
#10
#下面的表达式的输出结果为
x = 12
def f1():
    x = 3
    print(x)

def f2():
    x += 1
    print(x)

print(f1())
print(f2())



