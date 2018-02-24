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
        for i in range(ListLength):
            for j in range(1,ListLength-i):
                if bubbleList[j-1] >bubbleList[j]:
                    bubbleList[j-1],bubbleList[j] = bubbleList[j],bubbleList[j-1]
            print('第{}趟排序结果{}'.format(i+1,bubbleList))
    return bubbleList

def bubbleSortOptimize(bubbleList):
    """
    冒泡排序优化
    :param bubbleList: 
    :return: 
    """
    print("-------------------冒泡排序优化-------------------")
    if not bubbleList:
        return '空'
    for i in range(len(bubbleList)):
        found = False
        for j in range(1,len(bubbleList)-i):
            if bubbleList[j-1] > bubbleList[j]:
                bubbleList[j-1],bubbleList[j] = bubbleList[j],bubbleList[j-1]
                found = True
            if not found:
                break

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
    """
    希尔排序
    :param shellList: 
    :return: 
    """
    print("-------------------希尔排序-------------------")
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

def selectSort(selectList):
    """
    选择排序
    :param selectList: 
    :return: 
    """
    print("-------------------选择排序-------------------")
    if not selectList:
        return None
    for i in range(len(selectList)-1):
        k = i
        for j in range(i,len(selectList)): #k 为已知最小元素
            if selectList[j] < selectList[k]:
                k = j
        if i != k:      #检查是否要交换
            selectList[i],selectList[k] = selectList[k],selectList[i]
    return selectList


def heapSort(heapList):
    """
    堆排序
    :param heapList: 
    :return: 
    """
    print("-------------------堆排序-------------------")
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and heapList[child] < heapList[child + 1]:
                child += 1
            if heapList[root] < heapList[child]:
                heapList[root], heapList[child] = heapList[child], heapList[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range((len(heapList) - 2) // 2, -1, -1):
        sift_down(start, len(heapList) - 1)

    # 堆排序
    for end in range(len(heapList) - 1, 0, -1):
        heapList[0], heapList[end] = heapList[end], heapList[0]
        sift_down(0, end - 1)
    return heapList


if __name__ == '__main__':
    List = [9, 2, 1, 7, 6, 8, 5, 3, 4]
    print(bubbleSort(List))
    print(bubbleSortOptimize(List))
    print(insertSort(List))
    print(shellSort(List))
    print(selectSort(List))
    print(heapSort(List))
