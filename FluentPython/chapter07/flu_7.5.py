'''
@author：KongWeiKun
@file: flu_7.5.py
@time: 18-2-21 下午4:12
@contact: 836242657@qq.com
'''
"""
计算不断增加的系列值的平均值
"""
class Average():
    def __init__(self):
        self.series = []

    def __call__(self,new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)

def make_avrage():
    series = []

    def average(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len((series))

    return average

if __name__ == '__main__':
    avg = make_avrage()
    print(avg.__code__.co_varnames)
    print(avg(10))
    print(avg(11))

