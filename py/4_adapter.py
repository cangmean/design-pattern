"""
适配器模式: 提供一个外层的接口来兼容不同接口之间调用问题.
"""


class Synthesizer:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} synthesizer'.format(self.name)
    
    def play(self):
        return 'is playing an electronic song'


class Human:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return '{} the human'.format(self.name)
    
    def speak(self):
        return 'says hello'


class Computer:

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'the {} computer'.format(self.name)
    
    def execute(self):
        return 'executes a program'


class Adapter:

    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)
    
    def __str__(self):
        return str(self.obj)


def main():
    """ 通过适配器模式把不同的接口, 统一成一个接口输出"""
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for obj in objects:
        print('{} {}'.format(str(obj), obj.execute()))