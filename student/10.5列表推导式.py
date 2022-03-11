fruits = ['one', 'two', 'three', 'four', 'five', 'six']
new_list = []

# 一般情况下
"""
for x in fruits:  # 先循环遍历fruits数组
    if 'o' in x:  # 作判定条件 （若fruits中的某项含有'o'）
        new_list.append(x)  # 执行该流程（将上述判断成功后循环到的该项追加至new_list中）
print(new_list)

"""

# 使用了 推导式

"""
new_list = [x for x in fruits if 'o' in x]
print(new_list)
"""


"""
new_list = [x for x in range(10) if x < 7]
print(new_list)
"""



