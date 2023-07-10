# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第二章的内容
展示了Numpy多维数组之间的堆叠（这里的堆叠是指维度域的堆叠,所以时刻想到可以用array.shape查看维度）
也可以理解为不同维度如行维度、列维度、深维度的拼接
理解难点在于一些函数对一维数组的处理会转化为二维。所以对于一维要单独考虑
使用命令行语句："python stacking.py"来执行这个程序
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解,修改了少量代码如变量命名等
# 附加了对一维数组的讨论
# 代码通过pylint检测
import numpy as np

if __name__ == "__main__":
    print("In: a = arange(9).reshape(3,3)")
    print("In: a")
    array_a = np.arange(9).reshape(3, 3)
    print("Out: array({})".format(array_a))
    print("In: b = 2 * a")
    array_b = 2 * array_a
    print("In: b")
    print("Out: array({})".format(array_b))

    # 为显示好看这里加了一行换行
    print()
    # 多维数组(维度>1)，numpy.hstack()进行的列维度堆叠表现为：行维度不变，列维度增加
    # 参数是一个元组类型,如(a,b)
    print("In: hstack((a,b))")
    array_c = np.hstack((array_a, array_b))
    print("Out: array({})".format(array_c))
    # 官方文档给出的定义是：对数组进行水平向（列）堆叠。该过程与第二维度（axis=1）的数组拼接（concatenation）是等价的，
    # 但是1维数组除外，因其只具有一个维度，故是在第一个维度进行拼接。
    # 对于一维数组(N,)，该方法首先将其转换为(1, N)形状，而后进行堆叠。
    print("In: concatenate((a,b),axis=1)")
    array_c = np.concatenate((array_a, array_b), axis=1)
    print("Out: array({})".format(array_c))

    # 为显示好看这里加了一行换行
    print()
    # 多维数组(维度>1)，np.vstack()在行纬度的堆叠体现在：行维度增加，列维度保持不变。
    print("In: vstack((a,b))")
    array_c = np.vstack((array_a, array_b))
    print("Out: array({})".format(array_c))
    # 官方文档给出的定义是：对数组进行垂直向（行）堆叠。该过程与第一维度（axis=0）的数组连接（concatenation）是等价的。
    # 对于一维数组(N,)，该方法首先将其转换为(1, N)形状，而后进行堆叠。
    print("In: concatenate((a,b),axis=0)")
    array_c = np.concatenate((array_a, array_b), axis=0)
    print("Out: array({})".format(array_c))

    # 为显示好看这里加了一行换行
    print()
    # 多维数组(维度>1)，numpy.dstack()进行的深度维度堆叠表现为：行维度不变，列维度不变，深维度增加
    # 参数是一个元组类型,如(a,b)
    # 当数组为2维数组(M,N)时，会将其维度改变为(M,N,1)然后沿着第三根轴进行拼接
    # 当数组为1维数组(N,)时，会将其改变为(1,N,1)然后沿着第三根轴进行拼接
    print("In: dstack((a,b))")
    array_c = np.dstack((array_a, array_b))
    print("Out: array({})".format(array_c))

    # 为显示好看这里加了一行换行
    print()
    # column_stack():
    # 一维数组(N,)会先转换为二维(N,1)然后做hstack()
    # 二维数组(N,M)和hstack()值相同
    print("In: oned = arange(2)")
    print("In: oned")
    array_a_1d = np.arange(2)
    print("Out: array({})".format(array_a_1d))
    print("In: twice_oned = 2 * oned")
    print("In: twice_oned")
    array_b_1d = 2 * array_a_1d
    print("Out: array({})".format(array_b_1d))
    print("In: column_stack((oned,twice_oned))")
    array_c_1d = np.column_stack((array_a_1d, array_b_1d))
    print("Out: array({})".format(array_c_1d))
    print("In: column_stack((a,b))")
    array_c = np.column_stack((array_a, array_b))
    print("Out: array({})".format(array_c))
    print("In: column_stack((a,b)) == hstack((a,b))")
    array_c = np.column_stack((array_a, array_b)) == np.hstack((array_a, array_b))
    print("Out: array({})".format(array_c))

    # 为显示好看这里加了一行换行
    print()
    # row_stack():
    # 一维数组(N,)会先转换为二维(1,N)和vstack()值相同
    # 二维数组(N,M)和vstack()值相同
    print("In: row_stack((oned, twice_oned))")
    array_c_1d = np.row_stack((array_a_1d, array_b_1d))
    print("Out: array({})".format(array_c_1d))
    print("In: row_stack((a,b))")
    array_c = np.row_stack((array_a, array_b))
    print("Out: array({})".format(array_c))
    print("In: row_stack((a,b)) == vstack((a,b))")
    array_c = np.row_stack((array_a, array_b)) == np.vstack((array_a, array_b))
    print("Out: array({})".format(array_c))

    # 为显示好看这里加了一行换行
    print()
    print("附加：一维数组的hstack()、vstack()、dstack()")
    # 这里额外测试一下一维数组的情况
    array_a = np.arange(9)
    array_b = 2 * array_a
    print("In: a")
    print("Out: array({})".format(array_a))
    print("In: b")
    print("Out: array({})".format(array_b))
    print("In: hstack((a,b))")
    # 对于一维数组(N,)，hstack()方法直接在这个维度进行堆叠。
    array_c = np.hstack((array_a, array_b))
    print("Out: array({})".format(array_c))
    # 为显示好看这里加了一行换行
    print()
    print("In: vstack((a,b))")
    # 对于一维数组(N,)，vstack()方法首先将其转换为(1, N)形状，而后进行堆叠。
    array_c = np.vstack((array_a, array_b))
    print("Out: array({})".format(array_c))
    # 为显示好看这里加了一行换行
    print()
    print("In: dstack((a,b))")
    # 对于一维数组(N,)，dstack()方法首先将其转换为(1,N,1)然后沿着第三根轴进行拼接
    array_c = np.dstack((array_a, array_b))
    print("Out: array({})".format(array_c))
