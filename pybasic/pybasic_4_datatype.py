#!/usr/bin/python3
# 第一个实例
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# 多个变量赋值
# Python允许你同时为多个变量赋值。例如：
a = b = c = 1
# 以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
# 您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "runoob"
# 以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c

# Number（数字）
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
# 此外还可以用 isinstance 来判断：
# 实例
a = 111
isinstance(a, int)
# True
# >>>
# isinstance 和 type 的区别在于：
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。
var1 = 1
var2 = 10
# 您也可以使用del语句删除一些对象引用。
# del语句的语法是：
# del var1[,var2[,var3[....,varN]]]
# 您可以通过使用del语句删除单个或多个对象。例如：
# del var
# del var_a, var_b
# 数值运算
# 实例
# >>>5 + 4  # 加法
# 9
# >>> 4.3 - 2 # 减法
# 2.3
# >>> 3 * 7  # 乘法
# 21
# >>> 2 / 4  # 除法，得到一个浮点数
# 0.5
# >>> 2 // 4 # 除法，得到一个整数
# 0
# >>> 17 % 3 # 取余
# 2
# >>> 2 ** 5 # 乘方
# 32
# 注意：
# 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
# 2、一个变量可以通过赋值指向不同类型的对象。
# 3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 4、在混合计算时，Python会把整型转换成为浮点数。

# String（字符串）
# Python中的字符串用单引号
# ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
# 字符串的截取的语法格式如下：
# 变量[头下标:尾下标]
#
# 加号 + 是字符串的连接符， 星号 * 表示复制当前字符串，紧跟的数字为复制的次数。实例如下：
# 实例
# # !/usr/bin/python3

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + "TEST")  # 连接字符串

# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。
# 实例
# >>>word = 'Python'
# >>> print(word[0], word[5])
# P n
# >>> print(word[-1], word[-6])
# n P

#list
list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like runoob'
    rw = reverseWords(input)
    print(rw)

# Tuple（元组）
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号()
# 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：
# 实例
# # !/usr/bin/python3

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# 实例
# >>>tup = (1, 2, 3, 4, 5, 6)
# >>> print(tup[0])
# 1
# >>> print(tup[1:5])
# (2, 3, 4, 5)
# >>> tup[0] = 11  # 修改元组元素的操作是非法的
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>>
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
# tup1 = ()    # 空元组
# tup2 = (20,) # 一个元素，需要在元素后添加逗号

# Set（集合）
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# # !/usr/bin/python3

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)  # a 和 b 的差集

print(a | b)  # a 和 b 的并集

print(a & b)  # a 和 b 的交集

print(a ^ b)  # a 和 b 中不同时存在的元素

# Dictionary（字典）
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 构造函数
# dict()
# 可以直接从键值对序列中构建字典如下：
# 实例
# >> > dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {'Taobao': 3, 'Runoob': 1, 'Google': 2}
#
# >> > {x: x ** 2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}
#
# >> > dict(Runoob=1, Google=2, Taobao=3)
# {'Runoob': 1, 'Google': 2, 'Taobao': 3}
# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()
# 等。
# 注意：
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用