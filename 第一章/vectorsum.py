# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第一章的内容
展示了使用标准Python和Numpy分别实现向量加法所需要的时间
使用命令行语句："python vectorsum.py num"来执行这个程序
其中num是一个正整数，表示向量的大小
处理逻辑：
第一个向量的值为连续的0到num这num个数的平方。例如num=3,这个向量为(0,1,4)
第二个向量的值为连续的0到num这num个数的立方。
程序会打印出这两个向量相加生成的新向量的最后两个元素值，以及相关过程运行的时间
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解
# 代码通过pylint检测
import sys
from datetime import datetime
import numpy as np


def numpy_sum(num):
    """
    采用numpy来实现
    """
    vector_a = np.arange(num) ** 2
    vector_b = np.arange(num) ** 3
    vector_c = vector_a + vector_b
    return vector_c


def python_sum(num):
    """
    采用标准python来实现
    """
    vector_a = [each_element ** 2 for each_element in range(num)]
    vector_b = [each_element ** 3 for each_element in range(num)]
    vector_c = []
    for each_element in range(num):
        vector_c.append(vector_a[each_element] + vector_b[each_element])
    return vector_c


if __name__ == "__main__":
    size = int(sys.argv[1])
    start_time = datetime.now()
    vector = python_sum(size)
    elapse_time = datetime.now() - start_time
    print("两个向量相加生成的新向量的最后两个元素值:{}".format(vector[-2:]))
    print("过程python_sum 运行的时间是:{}毫秒".format(elapse_time.microseconds))

    start_time = datetime.now()
    vector = numpy_sum(size)
    elapse_time = datetime.now() - start_time
    print("两个向量相加生成的新向量的最后两个元素值:{}".format(vector[-2:]))
    print("过程numpy_sum 运行的时间是:{}毫秒".format(elapse_time.microseconds))
