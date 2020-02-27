'''
访问字典里的值
把相应的键放入到方括号中，如下实例:
实例
# !/usr/bin/python
'''
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print("dict1['Name']: ", dict1['Name'])
print("dict1['Age']: ", dict1['Age'])


'''
向字典添加新内容的方法是增加新的键 / 值对，修改或删除已有键 / 值对如下实例:
实例
# !/usr
'''
dict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict2['Age'] = 8  # 更新 Age
dict2['School'] = "南高职"  # 添加信息

print("dict2['Age']: ", dict2['Age'])
print("dict2['School']: ", dict2['School'])

'''
删除字典元素
能删单一的元素也能清空字典，清空只需一项操作。
显示删除一个字典用del命令，如下实例：
实例
# !/usr/bin/python3
'''
dict3 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict3['Name']  # 删除键 'Name'
# dict3.clear()  # 清空字典
# del dict3  # 删除字典

print("dict3['Age']: ", dict3['Age'])
# print("dict3['School']: ", dict3['School'])

'''
字典键的特性
'''
# 字典值可以是任何的对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# 实例
# # !/usr/bin/python3

dict4 = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}

print("dict4['Name']: ", dict4['Name'])

# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
# 实例
# # !/usr/bin/python3

# dict5 = {['Name']: 'Runoob', 'Age': 7}

# print("dict5['Name']: ", dict5['Name'])


'''
字典字段的比较
获取字典中最大的值及其键：
'''
prices = {
    'A':123,
    'B':450.1,
    'C':12,
    'E':444,
}

max_prices = max(zip(prices.values(), prices.keys()))
print("max value and prices: ",max_prices)
# (450.1, 'B')
'''
字典可以通过以下方法调换 key和 value,当然要注意原始 value 的类型,必须是不可变类型：
'''
dic6 = {
    'a': 1,
    'b': 2,
    'c': 3,
}

reverse = {v: k for k, v in dic6.items()}

print(dic6)
print(reverse)
'''
用字典记录学生名字和分数，再分级:
#!/usr/bin/python3
'''
students= {}
write = 1
while write :
    name = str(input('输入名字:'))
    grade = int(input('输入分数:'))
    students[str(name)] = grade
    write= int(input('继续输入？\n 1/继续  0/退出'))
print('name  rate'.center(20,'-'))
for key,value in students.items():
    if value >= 90:
        print('%s %s  A'.center(20,'-')%(key,value))
    elif 89 > value >= 60 :
        print('%s %s  B'.center(20,'-')%(key,value))
    else:
        print('%s %s  C'.center(20,'-')%(key,value))
