'''
@author：KongWeiKun
@file: garage.py
@time: 18-1-30 下午2:11
@contact: 836242657@qq.com
'''
'''
有一个只有一个空地的停车场。 给定初始状态
停车场和最后的状态。 我们只允许每一步
移动一辆车
出其位置并将其移入空位。
目标是找出重新排列所需的最少运动
从初始状态到最终状态的停车场。

说初始状态是一个数组：

[1,2,3,0,4]，
1,2,3,4是不同的车，0是空的地方。

最后的状态是

[0,3,2,1,4]。
我们可以在初始数组中将1与0交换得到[0,2,3,1,4]等等。
每一步只用0交换
'''

def garage(initial,final):
    steps = 0
    while initial != final:
        zero = initial.index(0)
        if zero != final.index(0):
            car_to_move = final[zero]
            pos = initial.index(car_to_move)
            initial[zero], initial[pos] = initial[pos], initial[zero]
        else:
            for i in range(len(initial)):
                if initial[i] != final[i]:
                    initial[zero], initial[i] = initial[i], initial[zero]
                    break
        steps += 1
    return steps

if __name__ == '__main__':
    initial = [1, 2, 3, 0, 4]
    final = [0, 3, 2, 1, 4]
    print("initial:", initial)
    print("final:", final)
    print(garage(initial, final))