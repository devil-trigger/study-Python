# 基本形式
# 字典用于在键值对中存储数据值。字典是有序*、可变且不允许重复的集合。（从 Python 3.7 版开始，字典是有序的。在 Python 3.6 及更早版本中，字典是无序的。）
this_dict = {
    'name': 'thebee',
    'sex': 'man',
    'age': '16'
}

# 创建字典与访问
dict_thebee = {
    'id': '15555',
    'position': 'shenzhen',
    'model': 'professional'
}
print(dict_thebee['model'])

# 字典长度
print(len(this_dict))

# 数据类型
dict_alice = {
    'id': 12333,
    'sex': 'women',
    'age': '18',
    'type': False,
    'color': ['red', 'green', 'blue'],
    'data': {'sss', 'ddd', 'aaa'}
}
print(type(dict_alice))
