'''
@author：KongWeiKun
@file: bubble_sort.py
@time: 18-1-2 下午8:34
@contact: 836242657@qq.com
'''
'''
冒泡排序 一种交换排序
'''
def bubbleSort(input_list):
    if not input_list:
        return []
    sorted_list = input_list
    for i in range(len(sorted_list)):
        for j in range(i+1,len(sorted_list))[::-1]:
            if sorted_list[j-1]>sorted_list[j]:
                sorted_list[j],sorted_list[j-1] = sorted_list[j-1],sorted_list[j]
    return sorted_list
if __name__ == '__main__':
    input_list = [2, 6, 3, 7, 4, 3, 1]
    print('排序前:', input_list)
    sorted_list = bubbleSort(input_list)
    print('排序后:', sorted_list)
    s=[]
    k=[]
    for i in range(len(input_list)):
        s.append(i)
        for l in range(i+1,len(input_list))[::-1]:
            k.append(l)
    print(s)
    print(k)