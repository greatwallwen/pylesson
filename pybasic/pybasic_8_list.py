# 访问列表中的值
# !/usr/bin/python3

list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7];

print("list1[0]: ", list1[0])
print("list2[1:5]: ", list2[1:5])

# 更新列表

list = ['Google', 'Runoob', 1997, 2000]

print("第三个元素为 : ", list[2])
list[2] = 2001
print("更新后的第三个元素为 : ", list[2])

# 删除列表元素

list = ['Google', 'Runoob', 1997, 2000]

print("原始列表 : ", list)
del list[2]
print("删除第三个元素 : ", list)

# 嵌套列表
# 使用嵌套列表即在列表里创建其它列表，例如：
# >>>a = ['a', 'b', 'c']
# >>> n = [1, 2, 3]
# >>> x = [a, n]
# >>> x
# [['a', 'b', 'c'], [1, 2, 3]]
# >>> x[0]
# ['a', 'b', 'c']
# >>> x[0][1]
# 'b'

# 复制问题，其实可以用copy模块里 copy()函数解决，实例如下：
import copy

a = [1,2,3,4]
b = a
d = copy.copy(a)
b[0] = 'b'
print(a,b,d)
print(id(a),id(b),id(d))

# 还有一个就是用list自带的copy()方法,把重新开辟内存空间存储新列表。
original_list=[0,1,2,3,4,5,6,7,8]
copy_list=original_list.copy()
copy_list=copy_list+['a','b','c']
print("original_list:",original_list)
print("copy_list modify:",copy_list)

# 1、列表推导式书写形式：　　
# [表达式 for 变量 in 列表]
# 或者
# [表达式 for 变量 in 列表 if 条件]
# 2、举例说明：
# #!/usr/bin/python
# # -*- coding: utf-8 -*-

li = [1,2,3,4,5,6,7,8,9]
print ([x**2 for x in li])

print ([x**2 for x in li if x>5])

print (dict([(x,x*10) for x in li]))


print ([ (x, y) for x in range(10) if x % 2 if x > 3 for y in range(10) if y > 7 if y != 8 ])

vec=[2,4,6]
vec2=[4,3,-9]
sq = [vec[i]+vec2[i] for i in range(len(vec))]
print (sq)

print ([x*y for x in [1,2,3] for y in  [1,2,3]])

testList = [1,2,3,4]
def mul2(x):
    return x*2
print ([mul2(i) for i in testList])

