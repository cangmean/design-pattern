"""
命令模式: 提供一系列命令
优势:
    1. 不需要执行一个命令，命令可以按希望的执行.
    2. 调用命令的对象和执行命令的对象解耦， 调用者不需要知道命令的任何细节实现.
    3. 可以把命令组织起来， 这样调用者可以顺序执行它们.
"""

import os

verbose = True


class RenameFile:

    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest
    
    def execute(self):
        if verbose:
            print("[renaming '{}' to '{}']".format(self.src, self.dest))
        os.rename(self.src, self.dest)
    
    def undo(self):
        if verbose:
            print("[renaming '{}' back to '{}']".format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile:

    def __init__(self, path, text="hello world\n"):
        self.path, self.text = path, text
    
    def execute(self):
        if verbose:
            print("[creating file '{}']".format(self.path))
        with open(self.path, mode='w', encoding='utf8') as fd:
            fd.write(self.text)
    
    def undo(self):
        delete_file(self.path)


class ReadFile:

    def __init__(self, path):
        self.path = path
    
    def execute(self):
        if verbose:
            print("[reading file '{}']".format(self.path))
        with open(self.path, mode='r', encoding='utf8') as fd:
            print(fd.read(), end='')


def delete_file(path):
    if verbose:
        print("deleting file '{}'".format(path))
    os.remove(path)


def main():
    orig_name, new_name = 'file1', 'file2'
    commands = []
    for cmd in CreateFile(orig_name), ReadFile(orig_name), RenameFile(orig_name, new_name):
        commands.append(cmd)
    [c.execute() for c in commands]

    answer = input('reverse the executed commands? [y/n] ')
    if answer not in 'yY':
        print("the result is {}".format(new_name))
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError:
            pass

main()