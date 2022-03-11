# 当我们创建一个元组时，我们通常会为其分配值。这称为“打包”元组
fruits = ('one', 'two', 'three', 'four')

"""
(green, red, yellow, blue) = fruits  # 分别赋值
print(green)
print(red)
print(yellow)
print(blue)
"""

# *号赋值
"""
(green, red, *yellow) = fruits  # 分别赋值
print(green)
print(red)
print(yellow)
"""

"""
# 如果星号被添加到另一个变量名而不是最后一个，Python 将为变量赋值，直到剩余的值数量与剩余的变量数量匹配。
(green, *red, blue) = fruits
print(green)
print(red)
print(blue)
"""

# 遍历元组

"""
# 一般遍历
for i in fruits:
    print(i)
"""

"""
# 遍历索引号
for i in range(len(fruits)):
    print(fruits[i])
"""

# while 循环遍历
"""
i = 0
while i < len(fruits):
    print(fruits[i])
    i+=1
"""