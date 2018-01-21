import os
'''
元组拆包
'''

'''
元组的平行赋值
'''
lax_coordinates=(33.9425,-118.408056)#洛杉矶国际机场的经纬度
latitude,longtitude=lax_coordinates
print(latitude)


'''
不使用中间变量交换两个变量
'''
print('-----------------------------------------------------------------------------------------------------')
print('不使用中间变量交换两个变量')
a=20
b=40
b,a=a,b
print(a,b)

'''
用*运算符可以迭代对象拆开作为函数的参数
'''
print('-----------------------------------------------------------------------------------------------------')
print('用*运算符可以迭代对象拆开作为函数的参数')
print(divmod(20,8))
t=(20,8)
print(divmod(*t))
quotient,remainder=divmod(*t)
print(quotient,remainder)


'''
用*处理剩下的元素
'''
print('-----------------------------------------------------------------------------------------------------')
print('用*处理剩下的元素')
a,b,*rest=range(5)
print(a,b,rest)
print('*可以出现在赋值表达式的任意位置')
a,*b,c=range(4)
print(a,b,c)
*a,b,c=range(4)
print(a,b,c)

'''
让一个函数可以用元组的形式返回多个值 然后调用函数的代码就能够轻松的接受这些返回值
'''
print('-----------------------------------------------------------------------------------------------------')
print('让一个函数可以用元组的形式返回多个值 然后调用函数的代码就能够轻松的接受这些返回值')
print(os.path.split('/home/fsfsa/fsa/sd.txt'))#返回（path,last_part）
_,filename=os.path.split('/home/fsfsa/fsa/sd.txt') #('/home/fsfsa/fsa', 'sd.txt')
print(filename)

