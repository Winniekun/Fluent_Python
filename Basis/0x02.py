'''
@author：KongWeiKun
@file: 0x02.py
@time: 18-1-21 下午4:07
@contact: 836242657@qq.com
'''
'''
摘自学点儿编程吧
'''
print(7/2)
print(7//2)
print(7.0/2)
print(7.0//2)
#答案 3.5 3 3.5 3.0
#讲解 在python3 中 ‘/’总是 执行真除法 不管操作数的类型 都会返回浮点结果
#// 执行floor除法 截除掉余数并且针对整数操作数返回一个整数 如果有任何一个操作数为浮点数则返回浮点数

list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)

str1 = 'abc'
str2 = 'abc'
print(str1 is str2)
print(str1 == str2)

#与0x01中的第3题一样 注： 内存中只有一个字符串'abc'供str1 和 str2 共享 这个主要是
#因为在Python内部会暂时存储并重复使用短字符串 也就是在创建短字符串时会首先到字符串的内存区域中
#查找是否已经有该字符串相等的值存在 若果有则指向该内存 避免重新开辟内存

# list = [1,3,6,4]
# for i in list.sort():
#     print(i)
#list.sort 返回为none 针对列表自己内部进行排序
#也就是说 只有引用透明 即没有副作用的函数 才会有返回值
#x.sort()，很明显，改变了 x 的值，具有副作用，所以不应该有返回值。
#https://mail.python.org/pipermail/python-dev/2003-October/038855.html
