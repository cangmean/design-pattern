"""
策略模式: 在不同情况下，切换策略. 比如排序种不同场景下切换排序算法.
"""

def f1(n):
    print('f1 recived {} return {}'.format(n, n))
    return n


def f2(n):
    print('f2 recived {} return {}'.format(n, -n))
    return -n


def main():
    nums = [3, -5]
    for n in nums:
        if n >= 0:
            f1(n)
        else:
            f2(n)

if __name__ == '__main__':
    main()