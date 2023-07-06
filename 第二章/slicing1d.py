# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第二章的内容
展示了Numpy一维数组的切片操作
使用命令行语句："python slicing1d.py"来执行这个程序
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解,修改了少量代码如变量命名等
# 代码通过pylint检测
import numpy as np

if __name__ == "__main__":
    print("In: a = arange(9)")
    array_one = np.arange(9)
    # 选择一个数组的切片操作，从索引3到索引7（包含索引3不包含7）
    print("In: a[3:7]")
    # 这里原始的array_one[3:7]产生[3 4 5 6]，和书中有少许差异，请注意
    print("Out: array({})".format(array_one[3:7]))

    # 为显示好看这里加了一行换行
    print()
    # 选择一个数组的切片操作，从索引0到索引7步长是2
    print("In: a[:7:2]")
    print("Out: array({})".format(array_one[:7:2]))

    # 为显示好看这里加了一行换行
    print()
    # 对数组进行反转操作
    print("In: a[::-1]")
    print("Out: array({})".format(array_one[::-1]))


