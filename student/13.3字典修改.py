this_dict = {
    'name': 'thebee',
    'sex': 'women',
    'ago': 27
}

"""
# 普通更改
this_dict['sex'] = 'man'
print(this_dict)


# update()
this_dict.update({'name': 'ssss'})
print(this_dict)
"""

# 添加字典项各种方法
# 普通方法
"""
this_dict['type']=True
print(this_dict)
"""
# update()方法
"""
this_dict.update({'type':False})
print(this_dict)
"""

# 删除字典的各种方法
"""
this_dict.pop('sex')  # pop()方法删除具有指定键名的项
print(this_dict)
"""

"""
this_dict.popitem()  # popitem()方法删除最后插入的项目
print(this_dict)
"""

"""
del this_dict['name']  # del关键字删除与指定键名称的项目
print(this_dict)

del this_dict  # del关键字也可以 完全删除 字典 
"""

"""
this_dict.clear()  # clear()方法清空字典(与del完全删除不同，可以输出空{} )
print(this_dict)
"""
