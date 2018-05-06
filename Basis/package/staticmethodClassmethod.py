'''
@author：KongWeiKun
@file: staticmethodClassmethod.py
@time: 18-4-15 下午7:47
@contact: kongwiki@163.com
'''
'''
@staticmethod 和 @classmethod的区别
'''
# def foo(x):
#     print('executing foo %s')%x
#
# class A(object):
#     def foo(self,x):
#         print("executing foo %s")%(self,x)
#
#     @classmethod
#     def class_foo(cls,x):
#         print('executing class_foo(%s,%s)')(cls,x)
#
#     @staticmethod
#     def static_foo(x):
#         print('executing static_foo(%s)')%x
#
# # 与类的交互而不是和实例交互的方法
# # def get_no_of_instances(cls_obj):
# #     return cls_obj.no_inst
# # class Kls(object):
# #     no_inst = 0
# #     def __init__(self):
# #         Kls.no_inst = Kls.no_inst + 1
# # ik1 = Kls()
# # ik2 = Kls()
# # print(get_no_of_instances(Kls))
#
#
# # 只在类中运行而不在实例中运行的方法
# # def iget_no_of_instance(ins_obj):
# #     return ins_obj.__class__.no_inst
# # class Kls(object):
# #     no_inst = 0
# #     def __init__(self):
# #         Kls.no_inst = Kls.no_inst + 1
# # ik1 = Kls()
# # ik2 = Kls()
# # print(iget_no_of_instance(ik1))
#
# IND = 'ON'
# def checkind():
#     return (IND == 'ON')
# class Kls(object):
#      def __init__(self,data):
#         self.data = data
#      def do_reset(self):
#         if checkind():
#             print('Reset done for:', self.data)
#      def set_db(self):
#         if checkind():
#             self.db = 'new db connection'
#             print('DB connection made for:',self.data)
# ik1 = Kls(12)
# ik1.do_reset()
# ik1.set_db()
#
# class Kls(object):
#      def __init__(self,data):
#         self.data = data
#
#      @staticmethod
#      def checkind():
#          return (IND == 'ON')
#
#      def do_reset(self):
#         if checkind():
#             print('Reset done for:', self.data)
#      def set_db(self):
#         if checkind():
#             self.db = 'new db connection'
#             print('DB connection made for:',self.data)
# ik1 = Kls(12)
# ik1.do_reset()
# ik1.set_db()
#
# class Date(object):
#
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         date1 = cls(day, month, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         day, month, year = map(int, date_as_string.split('-'))
#         return day <= 31 and month <= 12 and year <= 3999
#
# date2 = Date.from_string('11-09-2012')
# print(date2)
# is_date = Date.is_date_valid('11-09-2012')
# print(is_date)

class B(object):

    def foo(self,x):
        print("executing foo|--{},{}--|".format(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo|--{},{}--|".format(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo |--{}--|".format(x))

b = B()
b.foo(1)
b.class_foo(1)
B.class_foo(1)
B.static_foo(1)
b.static_foo(1)