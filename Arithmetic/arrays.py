'''
@author：KongWeiKun
@file: arrays.py
@time: 18-1-23 下午9:12
@contact: 836242657@qq.com
'''
'''
定义一个20*5的二维数组，用来存储某班级20位学员的5门课的成绩；这5门课按存储顺序依次为：core C++，coreJava，Servlet，JSP和EJB。

（1）循环给二维数组的每一个元素赋0~100之间的随机整数。

（2）按照列表的方式输出这些学员的每门课程的成绩。

（3）要求编写程序求每个学员的总分，将其保留在另外一个一维数组中。

（4）要求编写程序求所有学员的某门课程的平均分。
'''
import random

def scores(score_list,course_list,student_num):
    course_name = len(course_list)
    every_score = [score_list[j][i] for j in range(course_name)
                                    for i in range(student_num)]
    every_total = [[score_list[i][j] for i in range(course_name)]
                                     for j in range(student_num)]
    every_total = [sum(every_total[i])for i in range(course_name)]

    ave_course = [sum(score_list[i])/20 for i in range(course_name)]

    return every_score, every_total, ave_course

if __name__ == '__main__':
    course_list = ['C++','Java','Servlet','JSP','EJB']
    student_num = 20
    score_list = [[random.randint(0,100) for i in range(student_num)]
                                        for j in range(len(course_list))]
    for i in range(len(course_list)):
        print("score of every one in {:8} is |{}| ".format(course_list[i],score_list[i]))
    print('\n')
    print("next is every one score in every course")
    for i in range(student_num):
        for j,course_name in enumerate(course_list):
            print("score of {} in {} is {}".format(i+1,course_name,score_list[j][i]))
    print('\n')
    print('next is student all score')

    every_total = [[score_list[i][j] for i in range(len(course_list))]
                   for j in range(student_num)]
    # print(score_list)
    single_total = []
    ave_total = []
    for i in range(student_num):
        print('学生{} 总成绩是 {}'.format((i+1),sum(every_total[i])))
        single_total.append(sum(every_total[i]))
    print('某一门课平均成绩')
    for i in range(len(course_list)):
        print(sum(score_list[i])/20)

    every_score, every_total, ave_course = scores(score_list,course_list,student_num)
    print(every_score)
    print(every_total)
    print(ave_course)







