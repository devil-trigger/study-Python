# 基本理解
"""
i = 1
while i < 6:  # 使用while循环，只要条件为真，我们就可以执行一组语句。
    print(i)
    i += 1
"""

# 中断声明
"""
# break中断while循环
i = 2
while i < 20:
    print(i)
    if i == 12:
        break
    i += 2
"""

# continue 声明
"""
i = 0
while i < 10:
    i += 1
    if i == 4:
        continue  # 用continue语句，我们可以停止当前的迭代，并继续下一个
    print(i)  # 未输出 4 （被continue停止了）
"""

# else语句
"""
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print('结束循环')
"""

