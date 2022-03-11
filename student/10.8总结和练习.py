"""
# append()

# clear()

# copy()

# count()

# extend()

# index()

# insetr()
"""

fruits = ['one', 'two', 'three', 'four', 'five', 'six']
# 打印fruits列表中的第二项
"""
print(fruits[1])
"""

# 将fruits列表中的值从“four”改为“kiwi”
"""
fruits[3] = 'kiwi'
print(fruits)
"""

# 使用 append 方法将“orange”添加到fruits列表中
"""
fruits.append('orange')
print(fruits)
"""

# 使用插入方法将“柠檬”添加为fruits列表中的第二项
"""
fruits.insert(2, '柠檬')
print(fruits)
"""

# 使用 remove 方法从fruits列表中删除“four”
"""
fruits.remove('four')
print(fruits)
"""

# 使用负索引打印列表中的最后一项
"""
print(fruits[-1])
"""

# 使用索引范围打印列表中的第三、第四和第五项
"""
print(fruits[2:5])
"""

# 使用正确的语法打印列表中的项目数
"""
for x in fruits:
    print(x)
"""