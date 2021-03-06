"""
观察者模式: 当一个对象状态改变时, 更新另外一组对象
"""

class Publisher:
    """ 发布者"""
    def __init__(self, observer):
        self.observers = []
    
    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Falied to add: {}'.format(observer))
    
    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except:
            print('Falied to remove: {}'.format(observer))
    
    def notify(self):
        """ 通知"""
        for observer in self.observers:
            observer.notify(self)


class DefaultFormatter(Publisher):
    """ 默认格式化"""

    def __init__(self, name):
        super().__init__(self)
        self.name = name
        self._data = 0
    
    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now hex data = {}".format(type(self).__name__, publisher.name, hex(publisher.data)))


class BinaryFormatter:

    def notify(self, publisher):
        print("{}: '{}' has now bin data = {}".format(type(self).__name__, publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)
    print()

    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)
    print()

    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)
    print()

    df.remove(hf)
    df.data = 40
    print(df)
    print()

    df.remove(hf)
    df.add(bf)
    df.data = 'hello'
    print(df)
    print()

    df.data = 15.8
    print(df)

if __name__ == '__main__':
    main()