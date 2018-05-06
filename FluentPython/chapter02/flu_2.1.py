'''
列表推导和可读性
'''
#转化为Unicode码
symbols='$&*@'
codes=[]
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

#转化为Unicode另一种方法
symbols='$&*@'
codes=[ord(symbol) for symbol in symbols]
print(codes)