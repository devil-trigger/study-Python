# 基本
"""
fruits = ['apple', 'banana', 'orange', 'cherry']
for x in fruits:
    print(x)  # 依次遍历数组中的每一项
"""

# 遍历字符串
"""
my_text = 'hello world'
for x in my_text:
    print(x)  # 依次遍历字符串内的每一项（包括空格）
"""

# 中断声明
"""
my_list = ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
for x in my_list:
    print(x)
    if x == 'ddd':
        break  # 因中断未输出 'eee'
"""

# continue
"""
this_list = ['aaa', 'bbb', 'ccc', 'ddd']
for x in this_list:
    if x == 'ccc':
        continue  # 使用continue语句，我们可以停止循环的当前迭代，并继续下一个
    print(x)  # 类似于数组的全部内容打印一遍，除了 'ccc'
"""

# range()函数
"""
for x in range(10):
    # 要循环一组代码指定的次数，我们可以使用range()函数，的范围（）函数返回由1个数字，通过默认从0开始，并递增的顺序（缺省），并结束在指定次数。
    print(x)
"""

# 嵌套循环
"""
color_list = ['red', 'blue', 'orange', 'white']
my_list = ['apple', 'banana', 'orange']
for x in color_list:
    for y in my_list:
        print(x,y)
"""

# pass语句
"""
for x in [1,2,3,5,5,67,8]
    pass
"""