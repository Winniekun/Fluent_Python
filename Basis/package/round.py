'''
@author：KongWeiKun
@file: round.py
@time: 18-4-11 下午8:33
@contact: kongwiki@163.com
'''
'''
round 对浮点数执行指定精度运算 或者对整数进行舍入运算
当一个值刚好在两个边界的中间的时候
round 函数返回离它最近的偶数
也就是说，对1.5或者2.5的舍入运算都会得到2。
'''
print(round(1.2346466,2))
print(round(-1.2356466,2))
print(round(12345354,-2))
a = 2.1
b = 4.2
print(a+b)
