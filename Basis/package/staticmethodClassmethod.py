'''
@author：KongWeiKun
@file: staticmethodClassmethod.py
@time: 18-4-15 下午7:47
@contact: kongwiki@163.com
'''
'''
@staticmethod 和 @classmethod的区别
'''
class Myclass:
    def method(self):
        """
        
        :rtype: 
        """
        return 'instance method called',self

    @classmethod
    def classmethod(cls):
        return 'class method called',cls

    @staticmethod
    def staticmethod():
        return 'static method called'


obj = Myclass()
print(obj.method())
print(obj.classmethod())
print(obj.staticmethod())
print("--------------------------------------")
class Kls(object):
    def __init__(self,data):
        self.data = data

    def printed(self):
        print(self.data)

ik1 = Kls('arun')
ik2 = Kls('seema')
ik1.printed()
ik2.printed()