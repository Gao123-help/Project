"""
（1）类里面有对象属性也有类属性，对象属用于描述一个实例化的对象。比如person对象的姓名、性别等
（2）类属性用于描述一个类的特性，比如person类到底创建了几个实例count
（3）类方法用于访问操作类属性
"""


class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    def getname(self):
        print(self.name)
    @classmethod
    def getcount(cls):
        print(f"对象被创建了{cls.count}次")





