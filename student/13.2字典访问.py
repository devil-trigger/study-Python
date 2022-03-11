this_dict = {
    'name': 'bee',
    'sex': 'women',
    'age': 60

}
# 访问键名
"""
x = this_dict['sex']
print(x)

y = this_dict.get('age')
print(y)
"""

# 访问健
"""
z = this_dict.keys()
print(z)

this_dict['type'] = True
print(z)
"""

# 获取值
"""
a = this_dict.values()
print(a)  # values()方法将返回字典中所有值的列表,输出一个list

b = this_dict.items()
print(b)  # items()方法将返回字典中的每个项目，作为列表中的元组
"""

# 要确定字典中是否存在指定的键
if 'name' in this_dict:
    print('存在')
else:
    print('不存在')

