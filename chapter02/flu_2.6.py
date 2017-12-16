'''
@author：KongWeiKun
@file: flu_2.6.py
@time: 17-12-16 下午9:01
@contact: 836242657@qq.com
'''
'''
序列的增量赋值
'''
l=[1,2,3]
print(id(l))

l+=l
print(l)
print(id(l))

t=(1,2,3)
print(id(t))
t+=t
print(t)
print(id(t))

# s=(1,2,[30,40])
# s[2]+=[50,60]
