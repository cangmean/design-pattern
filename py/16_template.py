"""
模板模式: 通过把重复的抽象出来， 消除冗余.
"""

class Animal:

    def __init__(self, name):
        self.name = name
    
    def echo(self):
        raise NotImplementedError('Not Implemented')

class Dog(Animal):

    def echo(self):
        return 'wang wang ...'


class Cat(Animal):

    def echo(self):
        return 'miao miao ...'
