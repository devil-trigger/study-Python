'''
# 数组分配赋值
arrs = ['tom', 'jerry', 'alice']
x, y, z = arrs
print(x, y, z)
'''

'''
# 输出变量
g = 'the bee'
print(g + "很靓仔")
'''

'''
# 变量相互赋值
a = 'the'
b = 'bee'
z = a+b
print(z)
'''

'''
# 全局变量与局部变量
x = 'thebeee'
def myFun():
    b='bee'
    print(x+'很靓仔')

myFun()  #这x是全局变量 ，函数内外都能访问
print(b) # 报错，b只是myFun内的变量，只能在函数内部访问
'''

# 全局关键字
x = 'thebee'


def my_fun():
    global x
    x = 'tom'


my_fun()
print(x)  # global 关键字 能改变全局变量的值
