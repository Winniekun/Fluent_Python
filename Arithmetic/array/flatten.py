'''
@author：KongWeiKun
@file: flatten.py
@time: 18-1-29 下午3:22
@contact: 836242657@qq.com
'''
'''
实施平坦化阵列。
给定一个可能包含嵌套数组的数组，
给一个单一的结果数组。
函数flatten（输入）{
}
例：
输入：var input = [2,1，[3，[4,5]，6]，7，[8]];
弄平（输入）
输出：[2，1，3，4，5，6，7，8]
'''
def list_flatten(l, a=None):
    a = list(a) if isinstance(a, (list, tuple)) else []
    for i in l:
        if isinstance(i, (list, tuple)):
            a = list_flatten(i, a)
        else:
            a.append(i)
    return a

a = [2,1,[3,[4,5],7,[8]]]
print(list_flatten(a))

