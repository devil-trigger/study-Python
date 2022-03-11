fruits = {"apple", "banana", "cherry"}

# 检查fruits集中是否存在“apple”
"""
if 'apple' in fruits:
    print('存在apple')
else:
    print('不存在')
"""

# 使用 add 方法将“orange”添加到fruits集中
"""
fruits.add('hello world')
print(fruits)
"""

# 使用正确的方法将多个项目（more_fruits）添加到fruits 集中。
"""
more_fruits = ['aaa', 'bbb', 'ccc', 'ddd']
fruits.update(more_fruits)
print(fruits)
"""

# 使用 remove 方法从fruits 集中删除“banana
"""
fruits.remove('cherry')
print(fruits)
"""

# 使用discard方法从fruits 集中删除“banana”
"""
fruits.discard('banana')
print(fruits)
"""