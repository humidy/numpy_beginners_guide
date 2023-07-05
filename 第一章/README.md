# Numpy 初学者指南第一章代码说明

&emsp;&emsp;运行代码前，需要保证你的系统上已经安装好*Python*和*Numpy*

&emsp;&emsp;这一章包含一个程序，用于展示使用标准*Python*和*Numpy*分别实现向量加法所需要的时间，以体现*Numpy*中特定数据结构性能的优越性。可键入如下指令来执行该程序

```shell
python vectorsum.py n
```
&emsp;&emsp;其中参数n是一个正整数，例如：
```shell
python vectorsum.py 1000
```

&emsp;&emsp;第一个向量的值为连续的0到num这num个数的平方。例如num=3,这个向量为(0,1,4)

&emsp;&emsp;第二个向量的值为连续的0到num这num个数的立方。

&emsp;&emsp;程序会打印出这两个向量相加生成的新向量的最后两个元素值，以及相关过程运行的时间
