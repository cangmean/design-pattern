"""
享元模式: 把多个对象共同部分存起来.
"""

from enum import Enum

TreeType = Enum('TreeType', 'apple_tree cherry_tree peach_tree')


class Tree:

    pool = {}

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))