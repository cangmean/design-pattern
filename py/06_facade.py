"""
外观模式: 为复杂系统创建一个快捷方式.
"""

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class Server(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self):
        pass
    
    def __str__(self):
        return self.name
    
    @abstractmethod
    def boot(self):
        pass
    
    @abstractmethodd
    def kill(self, restart=True):
        pass


class FileServer(Server):

    def __init__(self):
        """ 初始化文件服务进程"""
        self.name = 'FileServer'
        self.state = State.new
    
    def boot(self):
        print('booting the {}'.format(self))
        self.state = State.running
    
    def kill(self, restart=True):
        print('killing {}'.format(self))
        self.state = State.restart if restart else State.zombie
    
    def create_file(self, user, name, permissions):
        print("trying to create the file '{}' for user '{}' with permissions {}".format(name, user, permissions))


class ProcessServer(Server):

    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new
    
    def boot(self):
        print('booting the {}'.format(self))
        self.state = State.running

    def kill(self, restart=True):
        print('killing {}'.format(self))
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        print("trying to create the process '{}' for user '{}'".format(name, user))


class OperatingSystem:
    """ 外观类， 把服务类操作细节隐藏起来， 通过外观模式调用"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        self.fs.boot()
        self.ps.boot()
    
    def create_file(self, user, name, permissions):
        return self.fs.create_file(usre, name, permissions)
    
    def create_process(self, user, name):
        return self.ps.create_process(user, name)