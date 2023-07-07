# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第二章的内容
展示了Numpy多维数组的形状变换操作
使用命令行语句："python shapemanipulation.py"来执行这个程序
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解,修改了少量代码如变量命名等
# 代码通过pylint检测
import numpy as np

if __name__ == "__main__":
    print("In: b = arange(24).reshape(2,3,4)")
    array_multi = np.arange(24).reshape((2, 3, 4))
    print("In: b")
    print("Out: array({})".format(array_multi))
    # 将多维数组转化为一维的形式
    # 返回的新数组是原数组的视图（浅拷贝）,两个数组共享相同的内存，修改新数组会导致原数组发送改变
    print("In: b.ravel()")
    print("Out: array({})".format(array_multi.ravel()))

    # 为显示好看这里加了一行换行
    print()
    # 将多维数组转化为一维的形式
    # 返回的新数组是原数组的副本（深拷贝）,两个数组相互独立，对新数组的修改不会影响原数组
    print("In: flatten()")
    print("Out: array({})".format(array_multi.flatten()))

    # 为显示好看这里加了一行换行
    print()
    # 设置多维数组的形状,直接改变原数组的形状
    print("In: b.shape=(6,4)")
    array_multi.shape = (6, 4)
    print("In: b")
    print("Out: array({})".format(array_multi))

    # 为显示好看这里加了一行换行
    print()
    # 多维数组转置，不改变原数组，返回原数组的转置
    print("In: b.transpose()")
    print("Out: array({})".format(array_multi.transpose()))

    # 为显示好看这里加了一行换行
    print()
    # 设置多维数组的形状,功能同reshape(),但其没有返回值，直接修改原数组
    # reshape()
    print("In: b.resize((2,12))")
    print("In: b")
    array_multi.resize((2, 12))
    print("Out: {}".format(array_multi))
