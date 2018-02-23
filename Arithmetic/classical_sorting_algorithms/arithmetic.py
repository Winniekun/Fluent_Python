'''
@author：KongWeiKun
@file: arithmetic.py
@time: 18-2-23 上午9:11
@contact: 836242657@qq.com
'''
'''
经典排序算法
'''
def bubbleSort(bubbleList):
    """
    冒泡排序
    :param bubbleList: 
    :return: 
    """
    ListLength = len(bubbleList)
    print("-------------------冒泡排序-------------------")
    if ListLength:
        for i in range(ListLength-1):
            for j in range(0,ListLength-1-i):
                if bubbleList[j] >bubbleList[j+1]:
                    bubbleList[j],bubbleList[j+1] = bubbleList[j+1],bubbleList[j]
            print('第{}趟排序结果{}'.format(i+1,bubbleList))
    return bubbleList

def insertSort(insertList):
    """
    插入排序
    :param insertList: 
    :return: 
    """
    print("-------------------插入排序-------------------")
    if not insertList:
        return "空"

    for i in range(1,len(insertList)):
        x = insertList[i]
        j =i
        while j > 0 and insertList[j-1] > x:
            insertList[j] = insertList[j-1] #反序逐个后移元素 确定插入位置
            j -= 1
        insertList[j] = x
    return insertList

def shellSort(shellList):
    n = len(shellList)
    gap = int(n/2) #初始步长
    while gap >0:
        for i in range(gap,n):
            temp = shellList[i] # 每个步长进行插入排序
            j = i
            while j >= gap and shellList[j-gap] >temp:
                shellList[j] = shellList[j-gap]
                j -= gap
        gap = int(gap/2)
    return shellList

if __name__ == '__main__':
    List = [3, 4, 1, 2, 5, 8, 0]
    print(bubbleSort(List))
    print(insertSort(List))
    print(shellSort(List))

