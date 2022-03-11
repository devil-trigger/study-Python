"""
1 capitalize() 将第一个字符转换为大写
2 casefold() 将字符串转换为小写
3 center() 返回一个居中的字符串
4 count() 返回指定值在字符串中出现的次数
5 encode() 返回字符串的编码版本
6 endswith() 如果字符串以指定的值结尾，则返回 true
7 join() 将可迭代的元素连接到字符串的末尾
8 find() 在字符串中搜索指定值并返回找到它的位置
9 format() 初始化字符串中的指定值
10 index() 在字符串中搜索指定值并返回找到它的位置
"""

# 练习

# 使用 len 方法打印字符串的长度。
x = 'What are you talking about?'
print(len(x))

# 获取字符串 txt 的第一个字符。
y = 'hello world'
print(y[0])

# 获取从索引 2 到索引 4 的字符。
z = 'Raymage'
print(z[2:4])

# 返回开头或结尾没有任何空格的字符串
a = ' How do you do? '
print(a.strip())

# 将 b 的值转换为大写。
b = 'my name is thebee'
print(b.upper())

# 将 c 的值转换为小写
c = 'Game Over'
print(c.lower())

# 用 J 替换字符 H。
txt = 'Hello world'
print(txt.replace('l', 'H'))

# 插入正确的语法以添加名字参数的占位符
text = 'my name is {}'
name = 'thebee'
print(text.format(name))


