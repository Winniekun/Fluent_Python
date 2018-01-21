'''
@author：KongWeiKun
@file: 0x01.py
@time: 18-1-21 下午3:47
@contact: 836242657@qq.com
'''
'''
摘自python之禅公众号
'''
import keyword
# 1
# a)eval b)assert c)nonlocal d)pass 哪个不是python3中的关键字
#答案 a
print(keyword.kwlist)
a = ['eval','assert','nonlocal','pass']
for i in a:
    print(keyword.iskeyword(i))

#2
#3*1**3值为多少
print(3*1**3)
#解释：运算的优先级


#3
#下列两个表达式的输出内容是什么
a = 1
b = 1
# a is b 结果为？
print('第三题')
print(a is b)

a = 998
b = 998
#a is b 结果为？
print(a is b )
print('\n')
#讲解 : is 比较对象的内存地址 只有两个对象都指向相同的地址才返回true
# == 比较的是对象的值 值相同的两个对象内存地址不一定相同
# 值为300的两个整数在内存中是两个不同的对象 介于[-5,256]的整数 值相同的整数会共享一个对象
# 所以内存中不管出现多少个数值为1的对象 都表示为同一个对象

#4
#下面函数的返回只是什么
def func(a):
    a = a + '2'
    a = a*2
    return a
print(func('hello'))
#讲解 +不仅支持数字+操作 也支持列表

#5
#在python中 表达式 0.1+0.2==0.3 的返回是
print(0.1+0.2)
#讲解 在python中 数值对象都是用二进制来表示的 浮点数也不例外
# 但不是所有浮点数都能用二进制精确表示 一个浮点数转化为二进制就是不断地×2 取其整数部分


#6
#表达式~~~5的值是多少
print(~~~5)
#-6
#讲解 ~为按位取反 即对整数的二进制按位取反 5表示为二进制为00000101
# 按位取反后 11111010 这串二进制在计算机中以补码的形式存储 操作也是以补码进行操作
# 需要将其转化为原码才知道它代表的真实数值 然后三次取反和一次取反是一样的
# 将第一次的补码转化为原码即可
# 补码转原码 和 原码转补码 一样 负数第一位为1 其余为按位取反 后在最后以为+1
#7
#表达式bool('False')的返回值
print(bool('False'))
#'False'在这里为一个字符串

#8
#表达式True==False==False的值
print(True==False==False)
#链式比较 True==False==False 等价于True==False and False == False

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
#只要执行了break就不会执行else 反之亦然


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

#3 报错
#f2() 但你在局部作用域中给变量赋值 那么这个变量就会变成一个局部变量不管它在外部有没有初始化
print(~~~-1)

