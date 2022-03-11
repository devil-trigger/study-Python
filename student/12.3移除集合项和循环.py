# remove()
set_1 = {'one', 'two', 'three', 'four', 'five'}
set_1.remove('two')
print(set_1)

# discard()
set_2 = {'aaaa', 'bbbb', 'cccc', 'dddd'}
set_2.discard('cccc')
print(set_2)

# pop()
set_3 = {'list', 'dict', 'set', 'let'}
set_3.pop()  # 删除最后一项
print(set_3)

# clear()
set_4 = {'111', '222', '333', '444', '555'}
set_4.clear()
print(set_4)

# 循环
set_5 = {'aah', 'bobby', 'cocci', 'dddd'}
for i in set_5:
    print(i)