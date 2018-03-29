'''
@author：KongWeiKun
@file: flu_5.3.py
@time: 18-3-25 下午5:34
@contact: 836242657@qq.com
'''
fruit = ['strawbarry','fig','apple','cherry','raspberrry','banana']
s = sorted(fruit,key=lambda word: word[::-1])
print(s)
func = lambda x:x+1
print(func(1))
print(map( lambda x : x + 1, [1, 2, 3] ))
li = [11, 22, 33]
new_list = map(lambda a: a + 100, li)
for l in new_list:
    print(l)
li = [11, 22, 33]

new_list = filter(lambda arg: arg > 22, li)
for l in new_list:
    print(l)
#filter第一个参数为空，将获取原来序列

li = [11, 22, 33]

