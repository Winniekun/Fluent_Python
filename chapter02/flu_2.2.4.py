'''
列表生成器
可以使用列表生成器来初始化元组 数组或奇台序列类型
但生成器是更好的选择
生成器表达式是遵守了迭代器的协议 可以逐个产出元素
而不是先建立完整列表再把这个列表传递到摸个构造函数中
'''
import array

symbols='$&*@'
b=tuple(ord(symbol) for symbol in symbols)
print(b)

a=array.array('I',(ord(symbol) for symbol in symbols))
print(a)