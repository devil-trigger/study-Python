this_dict = {
    'name': 'Agito',
    'sex': 'man',
    'age': 17
}
# 复制字典
"""
# copy()
my_dict = this_dict.copy()
print(my_dict)

"""

"""
# dict(）函数
my_dict = dict(this_dict)
print(my_dict)
"""

# 嵌套字典
my_friends = {
    'tom':{
        'sex':'man',
        'age': 17
    },
    'jerry': {
        'sex': 'man',
        'age': 23
    },
    'alice': {
        'sex': 'man',
        'age': 15
    }
}
print(my_friends)
