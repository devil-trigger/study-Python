car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# 使用get方法打印汽车字典的“model”键的值
"""
print(car['model'])
"""

# 将“year”值从 1964 更改为 2020
"""
car.update({'year':2222})
print(car)
"""

# 将键/值对 “color” : “red” 添加到汽车字典中。
"""
car.update({'color':'red'})
print(car)
"""

# 使用 pop 方法从汽车字典中删除“model”
"""
car.pop('model')
print(car)
"""

# 使用clear方法清空car字典。
"""
car.clear()
print(car)
"""