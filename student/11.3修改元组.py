# 元组是不可更改的，这意味着一旦创建了元组，您就无法更改、添加或删除项目。
# 但是有一些解决方法：将元组转换为列表，更改列表，然后将列表转换回元组。

# 替换
"""
x = ('one', 'two', 'three', 'four', 'five')
y = list(x)
y[1] = 'student'
x = tuple(y)
print(x)
"""

# 添加项目值
"""
this_stuple = ('one', 'two', 'three', 'four', 'six')
y = list(this_stuple)
y.append('hhahahahahah')
this_stuple=tuple(y)
print(this_stuple)
"""

"""
this_stuple = ('222','333','334','335')
y = ('23444ssssss', )
this_stuple+=y
print(this_stuple)
"""

# 删除项目
"""
mystuple = ('one', 'two', 'three', 'four')
y = list(mystuple)
y.remove('four')
mystuple = tuple(y)
print(mystuple)
"""