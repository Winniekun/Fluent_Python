'''
@author：KongWeiKun
@file: bin_search.py
@time: 18-1-27 上午10:02
@contact: 836242657@qq.com
'''
'''
二分查找

list.index()无法应对大规模数据的查询，需要用其它方法解决，这里谈的就是二分查找
时间复杂度为O(n) 对于大规模的数据查询不适用
'''
a = [2,3,7,13,5]
print(a.index(13))

"""
二分查找的对象是：有序列表。这点特别需要注意。要把数组排好序先。怎么排序，可以参看我这里多篇排序问题的文章。

基本步骤：

从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
如果在某一步骤数组为空，则代表找不到。
这种搜索算法每一次比较都使搜索范围缩小一半。时间复杂度：O(logn)
"""

def binarySearch(lst ,value ,low ,high ):  #low high 为lst的查找范围
    if high < low:
        return -1
    mid = (low + high)//2 #floor 取整
    if lst[mid] > value:
        # print(lst[mid])
        return binarySearch(lst,value,low,mid)
    elif lst[mid] < value:
        return binarySearch(lst,value,mid,high)
    else:
        return mid



if __name__ == '__main__':
    l = range(50)
    print(binarySearch(l,48,0,49))
