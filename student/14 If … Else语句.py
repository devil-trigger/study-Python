"""
等于：a == b
不等于：a != b
小于：a < b
小于或等于：a <= b
大于：a > b
大于或等于：a >= b
"""

# if语句
"""
a = 66
b = 122
if a > b:
    print('没错，a确实大于b')
else:
    print('你错了')

"""

# else 、 and 、 or  嵌套if 、 pass

# else
"""
a = 54
b = 6556
if a > b:
    print('没错a>b')
else:  # else : 在其他关键字捕获任何未通过前面的条件抓获
    print('a不大于b')
"""

# and
"""
a = 333
b = '333'
c = 334
if a == b and a < c:  # and表示与后面条件一同进入判定
    print('两个条件都满足')
"""

# or 语句
"""
a = 233
b = 33
c = 553
if a > b or a < c:  # or表或，条件中的一项或多项成立即运行
    print('以上一项或者多项条件成立')
"""

# 嵌套if语句
"""
x = 41
if x > 22:
    print('你好，你通过了第一关')
    if x > 30:
        print('您通过了第二关')
        if x > 50:
            print('通过了第三关')
        else:
            print('未通过第三关')
    else:
        print('未通过第二关')
"""

# pass语句
"""
a = 33
b = 233
if a > b:
    pass

"""
