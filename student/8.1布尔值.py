# 比较
"""
print(10 > 5)  # True
print(10 == '10')  # False
print(10 < 9)  # False
"""

# if语句判断
"""
a = 123
b = 456
if a == b:
    print('这两个相等')
else:
    print('这两个不等')
"""

# 布尔真值
"""
# True如果它具有某种内容，几乎任何值都会被评估。任何字符串都是True，空字符串除外。
# 任何数字都是True，除了 0。任何列表、元组、集合和字典都是True，空的除外。
print(bool('abw'))
print(bool(12354))
print(bool(['apple', 'banana', 'berry']))
print(bool(''))
"""

# 函数返回布尔值
"""
def my_Fun(aa):
    if aa == '':
        return True
    else:
        return False


print(my_Fun('thebee'))
"""

# 部分内置函数返回布尔值
"""
x = 644.5
print(isinstance(x, int))
"""
