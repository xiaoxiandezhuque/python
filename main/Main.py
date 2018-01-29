#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print("你好，世界")
#
# val1 = [0, 1, 2, 3, 4, 5]
# for x in val1:
#     print(val1[x])
# def hah():
#     print("ha")
#
#
# if True:
#     print("true")

# print('%04d-%02d' % (3, 1))
# print('%.2f' % 3.1415926)
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()  # 初始序列
#     while True:
#         n = next(it)  # 返回序列的第一个数
#         yield n
#         it = filter(_not_divisible(n), it)  # 构造新序列
#
#
# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break


# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
#
# print(f1())
# import functools
#
# int2 =functools.partial(int,base=2)
#
# print(int2('10010'))
# print(type(122))
from datetime import datetime

print(datetime.now())

