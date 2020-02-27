# 1.1 命令行 python保留字
# import keyword
# keyword.kwlist

# 第一个注释
print("Hello, Python!")  # 第二个注释

# !/usr/bin/python3

# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python!")

if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
# print ("False")    # 缩进不一致，会导致运行错误

# 多行语句
# Python
# 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
item_one = item_two = item_three = 1
total = item_one + \
        item_two + \
        item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 数字(Number)类型
# 字符串(String)
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
# 执行下面的程序在按回车键后就会等待用户输入：
input("\n\n按下 enter 键后退出。")
# 以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

import sys;

# x = 'runoob'; sys.stdout.write(x + '\n')
# 使用交互式命令行执行，输出结果为：
# >>> import sys; x = 'runoob'; sys.stdout.write(x + '\n')
# 输出结果：runoob
# 输出结果：7            #表示字符数

# 多个语句构成代码组
# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite

# Print 输出
x = "a"
y = "b"
# 换行输出
print(x)
print(y)

print('---------')
# 不换行输出
print(x, end=" ")
print(y, end=" ")
print()

# import 与 from ... import


import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)

from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

#note
# 当字符串内容为浮点型要转换为整型时，无法直接用 int() 转换：
a='2.1'  # 这是一个字符串
print(int(a))
# 会报错 "invalid literal for int() "。
# 需要把字符串先转化成 float 型再转换成 int 型：
a='2.1'
print(int(float(a)))

