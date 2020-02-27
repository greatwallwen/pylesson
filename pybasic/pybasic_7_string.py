# Python访问字符串中的值
# !/usr/bin/python3

var1 = 'Hello World!'
var2 = "Runoob"

print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

# Python
# 字符串更新
# 你可以截取字符串的一部分并与其他字段拼接，如下实例：
# 实例(Python3.0 +)
# # !/usr/bin/python3

var1 = 'Hello World!'

print("已更新字符串 : ", var1[:6] + 'Runoob!')

# Python字符串格式化
print("我叫 %s 今年 %d 岁!" % ('小明', 10))

# Python三引号
# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。

para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print(para_str)

# f-string
# f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
#
# >>> name = 'Runoob'
# >>> 'Hello %s' % name
# 'Hello Runoob'
# f-string 格式话字符串以 f 开头，后面跟着字符串，字符串中的表达式用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去，实例如下：
# 实例
# >>> name = 'Runoob'
# >>> f'Hello {name}'  # 替换变量
#
# >>> f'{1+2}'         # 使用表达式
# '3'
#
# >>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
# >>> f'{w["name"]}: {w["url"]}'
# 'Runoob: www.runoob.com'

# 用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d。
# 在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：
# 实例
# >>> x = 1
# >>> print(f'{x+1}')   # Python 3.6
# 2
#
# >>> x = 1
# >>> print(f'{x+1=}')   # Python 3.8
# 'x+1=2'