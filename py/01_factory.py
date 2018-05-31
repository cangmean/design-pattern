"""
工厂模式: 解决对象创建问题, 可以申请创建一个对象，不需要知道是哪个类生成的.
"""

import json
import xml.etree.ElementTree as etree


class JSONConnector:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath):
    """ 工厂方法
    通过对象信息来判断创建哪个对象
    """
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))
    return connector(filepath)

'''
抽象工厂模式, 关联多个对象创建
'''

class Frog:
    """ 青蛙类"""

    def __init__(self, name):
        self.name = name
    
    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}!'.format(self, obstacle, obstacle.action()))
    
    def __str__(self):
        return self.name


class Bug:
    """ 虫子类"""

    def action(self):
        return 'eats it'
    
    def __str__(self):
        return 'a bug'


class FrogWorld:
    """ 青蛙的抽象工厂
    """

    def __init__(self, name):
        self.player_name = name
    
    def make_character(self):
        return Frog(self.player_name)
    
    def make_obstacle(self):
        return Bug()
    
    def __str__(self):
        return 'FrogWrold'


class Wizard:

    def __init__(self, name):
        self.name = name
    
    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}!'.format(self, obstacle, obstacle.action()))
    
    def __str__(self):
        return self.name

class Ork:

    def action(self):
        return 'kills it'
    
    def __str__(self):
        return 'an evil ork'


class WizardWorld:

    def __init__(self, name):
        self.player_name = name

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()
    
    def __str__(self):
        return 'WizardWorld'


class GameEnvironment:
    """ 工厂类"""

    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()
    
    def play(self):
        self.hero.interact_with(self.obstacle)