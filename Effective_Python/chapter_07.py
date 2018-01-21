'''
@author：KongWeiKun
@file: chapter_07.py
@time: 17-10-22 下午2:17
@contact: 836242657@qq.com
'''
'''
用列表推导取代map filter
'''
a=[1,2,3,4,5,6,7,8,9]
suqares=[x**2 for x in a]
print(suqares)
m=map(lambda x:x**2,a)
print(m)
q=[x**2 for x in a if x%2==0]
# print(q)
#内置map 和　filter 也可实现上述
altet=map(lambda x:x**2,filter(lambda x:x%2==0,a))
assert q==list(altet)
print(q)
