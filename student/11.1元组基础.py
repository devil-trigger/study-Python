"""
元组用于在单个变量中存储多个项目。
Tuple 是 Python 中用于存储数据集合的 4 种内置数据类型之一，其他 3 种是List、 Set和Dictionary
它们具有不同的性质和用法。
元组是一个集合是有序的和不可改变的。元组是用圆括号写的。
"""

# 定义
my_tuple = ('one', 'two', 'three', 'four', 'five')
print(my_tuple)

# 访问
print(my_tuple[2])

# 长度
print(len(my_tuple))

# 类型
print(type(my_tuple))

# 数据类型
tuple_1 = ('apple', 'ads', 'dew')
tuple_2 = (1, 2, 5, 2, 13, 5, 44, 1)
tuple_3 = (False, True, False)
tuple_4 = (True, 'Assess', 123123, False, 2222)

# 其他创建方式
tuple_5 = tuple(('sodded', 'qwerty', 12312323))
print(tuple_5)
