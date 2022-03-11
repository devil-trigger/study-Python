this_dict = {
    'name': 'cc',
    'address': 'guangdong',
    'ago': 51
}
# 遍历所有键名
"""
for x in this_dict:
    print(x)
"""

# 遍历所有值
"""
for x in this_dict:
    print(this_dict[x])
"""

# valuses() : values()方法可以返回字典的值
"""
for x in this_dict.values():
    print(x)
"""

# key() : keys()方法返回字典的键
"""
for x in this_dict.keys():
    print(x)
"""

# 综合
"""
# 使用以下 方法循环遍历keys和valuesitems()
for x,y in this_dict.items():
    print(x,y)
"""