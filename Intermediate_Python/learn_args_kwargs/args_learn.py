'''
@author：KongWeiKun
@file: args_learn.py
@time: 18-2-20 下午3:19
@contact: 836242657@qq.com
'''
"""
*args 是用来发送一个非键值对的可变数量的参数列表给一个函数.
"""
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)
if __name__ == '__main__':
    test_var_args('yasoob', 'python', 'eggs', 'test')