# 将字符串分配给变量
x = 'thebee'

# 多行字符串
y = """老夫聊发少年狂，
左牵黄，
右擎苍"""

# 字符串 单个 访问
z = "Hello, world"
print(z[7])

# 遍历字符串 （以变量z的内容为例）
"""
for x in z:
    print(x)
"""

# 字符串长度 （以变量z的内容为例）
"""
print(len(z))
"""

# 检查字符串，查找字符串是否有该内容 （以变量z的内容为例）
"""
print('wor' in z)  # True
print('ool' in z)  # False
"""

"""
if 'wor' in z:
    print('存在这个字符')
"""

"""
# 检查不存在该字符
if 'cc' not in z:
    print('是的，cc的确不存在变量z中')
"""
