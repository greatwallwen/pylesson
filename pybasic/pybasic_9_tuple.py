# 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:


tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print(tup3)

# 删除元组

tup = ('Google', 'Runoob', 1997, 2000)

print(tup)
del tup
print("删除后的元组 tup : ")
print(tup)

# 元组索引，截取
# >>> L = ('Google', 'Taobao', 'Runoob')
# >>> L[2]
# 'Runoob'
# >>> L[-2]
# 'Taobao'
# >>> L[1:]
# ('Taobao', 'Runoob')

# 关于元组是不可变的
# 所谓元组的不可变指的是元组所指向的内存中的内容不可变。
# >>> tup = ('r', 'u', 'n', 'o', 'o', 'b')
# >>> tup[0] = 'g'     # 不支持修改元素
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> id(tup)     # 查看内存地址
# 4440687904
# >>> tup = (1,2,3)
# >>> id(tup)
# 4441088800    # 内存地址不一样了

# Python元组的升级版本 -- namedtuple(具名元组)
import collections

# 两种方法来给 namedtuple 定义方法名
#User = collections.namedtuple('User', ['name', 'age', 'id'])
User = collections.namedtuple('User', 'name age id')
user = User('tester', '22', '464643123')

print(user)
collections.namedtuple('User', 'name age id')

# 创建一个具名元组，需要两个参数，一个是类名，另一个是类的各个字段名。
# 后者可以是有多个字符串组成的可迭代对象，或者是有空格分隔开的字段名组成的字符串（比如本示例）。
# 具名元组可以通过字段名或者位置来获取一个字段的信息。

'''
具名元组的特有属性:
类属性 _fields：包含这个类所有字段名的元组 类方法 _make(iterable)：
接受一个可迭代对象来生产这个类的实例 实例方法 _asdict()：
把具名元组以 collections.OrdereDict 的形式返回，可以利用它来把元组里的信息友好的展示出来
'''
from collections import namedtuple

# 定义一个namedtuple类型User，并包含name，sex和age属性。
User = namedtuple('User', ['name', 'sex', 'age'])

# 创建一个User对象
user = User(name='Runoob', sex='male', age=12)

# 获取所有字段名
print( user._fields )

# 也可以通过一个list来创建一个User对象，这里注意需要使用"_make"方法
user = User._make(['Runoob', 'male', 12])

print( user )
# User(name='user1', sex='male', age=12)

# 获取用户的属性
print( user.name )
print( user.sex )
print( user.age )

# 修改对象属性，注意要使用"_replace"方法
user = user._replace(age=22)
print( user )
# User(name='user1', sex='male', age=21)

# 将User对象转换成字典，注意要使用"_asdict"
print( user._asdict() )
# OrderedDict([('name', 'Runoob'), ('sex', 'male'), ('age', 22)])

