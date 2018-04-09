'''
@author：KongWeiKun
@file: fsdagg.py
@time: 18-4-8 下午5:12
@contact: kongwiki@163.com
'''
"""
combinations : 排列组合
如[a,b,c] 3元素排列 ===> ('a', 'b', 'c')
permutations : 每个元组由集合中所有元素的一个可能排列组成 
如[a,b,c] 3元素排列 ===> ('a', 'b', 'c')
                        ('a', 'c', 'b')
                        ('b', 'a', 'c')
                        ('b', 'c', 'a')
                        ('c', 'a', 'b')
combinations_with_replace : 重复使用元素
如[a,b,c] 3元素排列 ===> ('a', 'a', 'a')
                         ('a', 'a', 'b')
                         ('a', 'a', 'c')
                         ('a', 'b', 'b')
                         ('a', 'b', 'c')
                         ('a', 'c', 'c')
                         ('b', 'b', 'b')
                         ('b', 'b', 'c')
                         ('b', 'c', 'c')
                         ('c', 'c', 'c')

"""
from itertools import combinations,combinations_with_replacement,permutations
a = set(['a','a','a','d','e','a'])
print(a)
a = list(['a','a','a','d','e','a'])
print(a)
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print(x)
single = ['a','b','c']
for c in combinations(single,3):
    print("combiantions",c)
print('\t')
for l in combinations_with_replacement(single,3):
    print("combinations_with_replacement",l)
print('\t')
for d in permutations(single,3):
    print(d)