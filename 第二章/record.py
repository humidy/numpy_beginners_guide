# -*- coding:utf-8 -*-
"""
程序来自Numpy初学者指南第二章的内容
展示了Numpy的自定义一行记录的数据类型
使用命令行语句："python record.py"来执行这个程序
"""
# 来自《Numpy Beginners Guide》
# @humidy-2023-7
# 编写中文注解,修改了少量代码如变量命名等
# 代码通过pylint检测
import numpy as np

if __name__ == "__main__":
    # 该程序按照书中IPython打印出的格式原样输出，所以使用了很多print语句来打印信息,为了符合命名规范，程序内部把变量t改成了record_type
    print("In: t = dtype([('name', str_, 40), ('numitems', int32), ('price', float32)])")
    # 自己定义这个记录每个元素的类型，学过SQL的可以类比这有点像定义表结构的字段
    record_type = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
    print("In: t")
    print("Out: dtype({})".format(record_type))

    # 为显示好看这里加了一行换行
    print()

    # 注意这里我用的python3.x，字符编码已经变成了unicode，所以内部字符表示是U，书中显示是S是因为用的是python2.x,这个版本字符
    # 是用bytes表示，参见：np.sctypeDict中的键值 "S <class 'numpy.bytes_'>"
    print("In: t['name']")
    print("Out: dtype('{}')".format(record_type['name']))

    # 为显示好看这里加了一行换行
    print()
    print("In: itemz = array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)")
    item = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=record_type)
    print("In: itemz[1]")
    print("Out: {}".format(item[1]))
