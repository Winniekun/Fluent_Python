'''
@author：KongWeiKun
@file: chapter_04.py
@time: 17-10-21 下午9:17
@contact: 836242657@qq.com
'''
'''
从url中解码查询字符串
'''
from urllib.parse import parse_qs

def get_first_int(values,key,default=0):
    found=values.get(key,[''])
    if found[0]:
        print(int(found[0]))
    else:
        print(default)

my_values=parse_qs('red=5&blue=0&green=11',keep_blank_values=True)
print(repr(my_values))
print("red   ",my_values.get('red'))
red=my_values.get('red',[''])[0] or 0
green = my_values.get('green',[''])
if green[0]:
    print('Green = %d'%int(green[0]))
else:
    print(0)
# opacity = my_values.get('opacity',[''])[0] or 0
opacity = get_first_int(my_values,'opactity')
print('Red %r'%red)
print('opacity %r'%opacity)

