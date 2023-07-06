# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第二章的内容
展示了Numpy多维数组的切片操作
使用命令行语句："python slicing.py"来执行这个程序
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解,修改了少量代码如变量命名等
# 代码通过pylint检测
import numpy as np

if __name__ == "__main__":
    print("In: b = arange(24).reshape(2,3,4)")
    array_multi = np.arange(24).reshape((2, 3, 4))
    print("In: b.shape")
    print("Out: {}".format(array_multi.shape))
    print("In: b")
    print("Out: array({})".format(array_multi))

    # 为显示好看这里加了一行换行
    print()
    # 可以通过指定具体三个维度坐标值来获取多维数组中具体的元素值或元素集合，表述如下
    # 第一维第一个，第二维第一个，第三维第一个
    print("In: b[0,0,0]")
    print("Out: {}".format(array_multi[0, 0, 0]))

    # 为显示好看这里加了一行换行
    print()
    # 第一维不限制，第二维第一个，第三维第一个
    print("In: b[:,0,0]")
    print("Out: array({})".format(array_multi[:, 0, 0]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维不限制，第三维不限制
    print("In: b[0,:,:]")
    print("Out: array({})".format(array_multi[0, :, :]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维第二个，第三维不限制
    print("In: b[0,1,:]")
    print("Out: array({})".format(array_multi[0, 1, :]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维第二个，第三维不限制步长为2
    print("In: b[0,1,::2]")
    print("Out: array({})".format(array_multi[0, 1, ::2]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维不限制，第二维第二个，第三维不限制
    print("In: b[:,1,:]")
    print("Out: array({})".format(array_multi[:, 1, :]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维不限制，第三维第二个
    print("In: b[0,:,1]")
    print("Out: array({})".format(array_multi[0, :, 1]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维不限制，第三维最后一个
    print("In: b[0,:,-1]")
    print("Out: array({})".format(array_multi[0, :, -1]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维不限制反转，第三维最后一个
    print("In: b[0,::-1,-1]")
    print("Out: array({})".format(array_multi[0, ::-1, -1]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维第一个，第二维不限制步长为2，第三维最后一个
    print("In: b[0,::2,-1]")
    print("Out: array({})".format(array_multi[0, ::2, -1]))

    # 为显示好看这里加了一行换行
    print()
    # 选择第一维不限制反转，第二维不限制，第三维不限制
    print("In: b[::-1,:,:]")
    print("Out: array({})".format(array_multi[::-1, :, :]))
