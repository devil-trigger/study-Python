"""
Python 共有三种数字类型：

int
float
complex
要验证 Python 中任何对象的类型，请使用type()函数：
"""

# 1整数 ：Int 或 integer，是一个整数，正负，不带小数，长度不限。
"""
x = 1
y = 31546633
z = -100
print(type(x))
print(type(y))
print(type(z))
"""

# 2浮点数 ： 浮点数或“浮点数”是包含一位或多位小数的正数或负数。
"""
x = 1.263546
y = 1.0
z = -212.135446
print(type(x))
print(type(y))
print(type(z))
"""

# 3虚数复数写有“j”作为虚部
"""
x = 3 + 5j
y = 92j
z = -1j
print(type(x))
print(type(y))
print(type(z))
"""

# 4类型转换
"""
x = 1
y = 2.15
z = -8j

a = float(x)
b = int(y)
c = complex(x)
print(a)  # 1.0
print(b)  # 2
print(c)  # (1+0j)

print(type(a))
print(type(b))
print(type(c))
"""

# 5随机数 Python 有一个内置模块 random可以用来生成随机数。
"""
import random
print(random.randrange(1, 55))
"""
