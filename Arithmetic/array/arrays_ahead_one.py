'''
@author：KongWeiKun
@file: arrays_ahead_one.py
@time: 18-1-24 下午5:38
@contact: 836242657@qq.com
'''
'''
定义一个int型的一维数组，包含10个元素，分别赋值为1~10， 
然后将数组中的元素都向前移一个位置，
即，a[0]=a[1],a[1]=a[2],…
最后一个元素的值是原来第一个元素的值，然后输出这个数组。
'''

def ahead_one():
    a =[i+1 for i in range(10)]
    print(a)
    b = a.pop(0)
    a.append(b)
    return a

if __name__ == '__main__':
    print(ahead_one())