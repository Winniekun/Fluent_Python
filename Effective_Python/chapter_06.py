'''
@author：KongWeiKun
@file: chapter_06.py
@time: 17-10-22 下午1:58
@contact: 836242657@qq.com
'''
'''
在单次切片时　不同时指定start end stride
'''
a=['red','orange','yellow','green','blue','purple']
print(a[::2]) #每个两个进行切片
print(a[1::2])#从第2个开始　每隔两个切片
x='mongoose'
print(x[::-1])#反转　对字符串和ascii字符有用
# 对已经编码成utf-8字符串的unicode 字符来说无用
y='谢你'
w=y.encode('utf-8')#编码成utf-8
q=w[::-1]
# q.decode('utf-8')#用utf-8重新解码

# s=q.decode('utf-8')



