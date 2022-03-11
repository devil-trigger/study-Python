x = 'My Name is TheBee'

# 从字符串的开头截取 ： 获取从开始到位置 5 的字符（不包括在内）
print(x[:5])  # 与print(x[0:5])相同   ——> My Na

# 正向地从任意位置截取
print(x[3:8])  # Name

# 正向地从某一位置截取至末尾
print(x[3:])  # Name is TheBee

# 逆向截取
print(x[-9:-7])  # is

