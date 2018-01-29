'''
@author：KongWeiKun
@file: circular_counter.py
@time: 18-1-29 下午12:49
@contact: 836242657@qq.com
'''
'''
有人围坐在一起，
打印每三名成员，同时删除它们，
成员被删除后，下一个计数器立即开始。
打印，直到所有的成员用尽。
例如：
输入：考虑123456789成员坐在一个圆形的方式，
输出：369485271
'''
a = [1,2,3,4,5,6,7,8,9]

def josepheus(int_list,skip):
    skip = skip - 1 #列表下标从0开始
    idx = 0
    len_list = (len(int_list))
    con = []
    while len_list>0:
        idx = (skip+idx)%len_list
        con.append(int_list.pop(idx))
        len_list -= 1
    print(con)

josepheus(a,3)
