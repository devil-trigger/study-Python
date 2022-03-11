x = " How old are you?  "

# 小写转大写
print(x.upper())  # HOW OLD ARE YOU?

# 清除空格
print(x.strip())

# 替换字符
print(x.replace('o', 'e'))  # Hew eld are yeu?

# 拆分字符 (以传入的字符分割成数组)
print(x.split('o'))  # [' H', 'w ', 'ld are y', 'u?  ']

# 字符串拼接

y = "I'm ten years old"
print(x + "  I'm ten years old")
print(x + "  " + y)
