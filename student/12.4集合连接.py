set_1 = {'aaa', 'bbb', 'ccc', 'ddd'}
set_2 = {'apple', 'aaa', 'orange', 'banana', 'ccc'}

# 普通连接

"""
# 方法一
set_3 = set_1.union(set_2)
print(set_3)
"""

"""
# 方法二
set_1.update(set_2)
print(set_1)
"""

# 仅保留重复项
"""
set_2.intersection_update(set_1)
print(set_2)
"""

# 保留所有，但不保留重复项(与上一条相反)
"""
# symmetric_difference_update()方法将只保留两个集合中都不存在的元素
set_1.symmetric_difference_update(set_2)
print(set_1)
"""
