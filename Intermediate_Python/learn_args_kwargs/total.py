'''
@author：KongWeiKun
@file: total.py
@time: 18-2-20 下午3:24
@contact: 836242657@qq.com
'''
"""
那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：+
some_func(fargs, *args, **kwargs)
"""


def test_args_kwargs(arg1,arg2,arg3):
    print("arg1:",arg1)
    print("arg2:",arg2)
    print("arg3:",arg3)

if __name__ == '__main__':
    args = ("two",3,5)
    test_args_kwargs(*args)
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    test_args_kwargs(**kwargs)
