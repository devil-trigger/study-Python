# 创建函数与调用
"""
# 在 Python 中，函数是使用def 关键字定义的
def my_function():
    print('sss')


my_function()

# ——————————————————————————

def this_function(a):
    print(a)


this_function('hello world')
"""

# 参数 : 信息可以作为参数传递给函数。参数在函数名后的括号内指定。您可以根据需要添加任意数量的参数，只需用逗号分隔它们
"""
def the_function(a):
    print('我是'+a)


the_function('thebee')
"""

# 参数数量
"""
def that_function(a,b):
    print(a+'是'+b)


that_function('我', 'thebee')
"""

# 任意参数,*args
"""
def here_function(*info_list):
    print('我是' + info_list[1])


here_function('thebee', 'alice', 'tom')
"""

# 关键字参数
"""
def the_function(child3, child2, child1):
    print(child2 + '是最帅的', child1 + '和' + child3 + '次之')


the_function('alice', 'tom', 'jerry')
"""

# 任意关键字参数，**kwargs
# 如果您不知道有多少关键字参数将被传递到您的函数中，请**在函数定义中的参数名称之前添加两个星号。这样，该函数将接收一个参数字典，并可以相应地访问这些项目.
"""
def then_function(**kid):
    print('它的名字叫做' + kid['name'])


then_function(name='thebee', sex='man')
"""

# 默认参数值
"""
# 如果我们不带参数调用函数，它将使用默认值
def info_function(country='china'):
    print(country)


info_function('india')
"""

# 将列表作为参数传递
"""
# 如果你发送一个 List 作为参数，当它到达函数时它仍然是一个 List
def list_function(aa):
    for x in aa:
        print(x)


my_list = ['aaa', 'bbb', 'ccc', 'ddd']
list_function(my_list)
"""


# 返回值
"""
def return_function(x):
    return x * 3


print(return_function(5))
print(return_function(2))
print(return_function(167))
"""

# pass语句
# function定义不能为空，但如果您出于某种原因有一个function没有内容的定义，请放入pass语句中以避免出错
"""
def pass_function():
    pass
"""


