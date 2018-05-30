"""
建造者模式: 如果一个对象需要若干个部分组成， 才能创建好， 这时候使用建造者模式.
一般有具体类，建造者类, 指挥者类， 指挥者通过下发指令建造具体的类。
例如: 服务员收到订单后指示需要构造某种比萨，　厨师按步骤创建比萨.
"""

import time
from enum import Enum

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3


class Pizza:
    """ 比萨类"""

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name
    
    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:
    """ 玛格丽特比萨建造者"""

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5
    
    def prepare_dough(self):
        """ 准备面团"""
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)
    
    def add_sauce(self):
        """ 添加沙司"""
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        """ 添加材料"""
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.extend([PizzaTopping.double_mozzarella, PizzaTopping.oregano])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarella, oregano)')
    
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7
    
    def prepare_dough(self):
        """ 准备面团"""
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)
    
    def add_sauce(self):
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')
    
    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon')
        self.pizza.topping.extend([
            PizzaTopping.mozzarella, PizzaTopping.bacon,
            PizzaTopping.ham, PizzaTopping.mushrooms,
            PizzaTopping.red_onion, PizzaTopping.oregano
        ])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)')
    
    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:
    """ 指挥者"""

    def __init__(self):
        self.builder = None
    
    def construct_pizza(self, builder):
        self.builder = builder
        steps = ['prepare_dough', 'add_sauce', 'add_topping', 'bake']
        for step in steps:
            getattr(builder, step)()
    
    @property
    def pizza(self):
        return self.builder.pizza
