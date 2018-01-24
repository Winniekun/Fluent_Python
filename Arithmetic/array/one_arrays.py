'''
@author：KongWeiKun
@file: one_arrays.py
@time: 18-1-24 下午5:59
@contact: 836242657@qq.com
'''
'''
定义一个int型的一维数组 包含40个元素 用来存储每个学员的成绩 
循环产生40个0~100之间的随机整数
(1)将它们存储到一维数组中 然后统计成绩低于平均分的学员的人数 并输出出来 
(2)将这40个成绩按照从高到低的顺序输出出来
'''
import random

def make_score(num):
    score = [random.randint(0,100) for i in range(num)]
    return score

def less_average(scores,num):
    average = sum(scores)/num
    low = []
    for i,score in enumerate(scores):
        if score<average:
           low.append(score)
    return low,average

if __name__ == '__main__':
    num = 40
    score_list = make_score(num)
    print('40名学生分布')
    print(score_list)
    less,average = less_average(score_list,num)
    print('平均成绩')
    print(average)
    print('低于平均成绩')
    print(less)
    print('成绩降序排列')
    arr = sorted(score_list,reverse=True)
    print(arr)