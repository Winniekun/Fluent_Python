'''
@author：KongWeiKun
@file: 2018-02-17.py
@time: 18-2-20 下午5:05
@contact: 836242657@qq.com
'''
print({True: 'yes', 1: 'no', 1.0: 'maybe'})
print(True==1==1.0)
xs = dict()
xs[True] = 'yes'
xs[1] = 'no'
xs[1.0] = 'maybe'
print(xs)
print(['no','yes'][False])
print(['no','yes'][True])
ys = {1.0:'no'}
ys[True] = 'yes'
print(ys)
class AlwaysEquals:
    def __eq__(self, other):
        return True

    def __hash__(self):
        return id(self)

print(AlwaysEquals() == AlwaysEquals())
print(AlwaysEquals() == 42)
print(AlwaysEquals() == 'whaaat')
objects = [AlwaysEquals(),
               AlwaysEquals(),
               AlwaysEquals()]
print('测试')
print([hash(obj) for obj in objects])
print({AlwaysEquals(): 'yes', AlwaysEquals(): 'no'})
print(AlwaysEquals() == AlwaysEquals())



class SameHash:
    def __hash__(self):
        return 1
a = SameHash()
b = SameHash()
print(a == b)
print(hash(a),hash(b))
print({a:'a',b:'b'})
print(hash(True),hash(1),hash(1.0))