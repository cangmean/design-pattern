"""
解释器模式: 解析一门DSL(特定语言)
执行: pip install pyparsing

"""

from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Gate:

    def __init__(self):
        self.is_open = False
    
    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True
    
    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:

    def __init__(self):
        self.is_open = False
    
    def __str__(self):
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True
    
    def close(self):
        print('closing the garage')
        self.is_open = False


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress("->")
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token + argument)
    gate = Gate()
    garage = Garage()

    # DSL
    tests = (
        'open -> gate',
        'close -> garage',
    )
    open_actions = {
        'gate': gate.open,
        'garage': garage.open
    }
    close_actions = {
        'gate': gate.close,
        'garage': garage.close,
    }
    for t in tests:
        if len(event.parseString(t)) == 2:
            cmd, dev = event.parseString(t)
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
        if 'open' in cmd_str or 'turn on' in cmd_str:
            open_actions[dev_str]()
        elif 'close' in cmd_str or 'turn off' in cmd_str:
            close_actions[dev_str]()

if __name__ == '__main__':
    main()