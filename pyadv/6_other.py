'''
zip lambda map
'''
a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))  #需要加list来可视化这个功能
"""
zip 中的运算
"""
a=[1,2,3]
b=[4,5,6]
ab=zip(a,b)
print(list(ab))
for i,j in zip(a,b):
     print(i/2,j*2)
'''
lambda
'''
# lambda定义一个简单的函数，实现简化代码的功能，看代码会更好理解。
# fun = lambda x,y : x+y, #冒号前的x,y为自变量，冒号后x+y为具体运算。

fun= lambda x,y:x+y
x=int(input('x='))    #这里要定义int整数，否则会默认为字符串
y=int(input('y='))
print(fun(x,y))
'''
map
'''
def fun(x,y):
	return (x+y)
print(list(map(fun,[1],[2])))
print(list(map(fun,[1,2],[3,4])))

'''
copy&deepcopy
'''
#id的例子
import copy
a=[1,2,3]
b=a
print(id(a))
"""
4382960392
"""
print(id(b))
"""
4382960392
"""
id(a)==id(b)    #附值后，两者的id相同，为true。
#True
b[0]=222222  #此时，改变b的第一个值，也会导致a值改变。
print(a,b)
#[222222, 2, 3] [222222, 2, 3] #a,b值同时改变

# 浅拷贝
# 当使用浅拷贝时，python只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。看代码：

import copy
a=[1,2,3]
c=copy.copy(a)  #拷贝了a的外围对象本身,
print(id(c))
# 4383658568
print(id(a)==id(c))  #id 改变 为false
# False
c[1]=22222   #此时，我去改变c的第二个值时，a不会被改变。
print(a,c)
# [1, 2, 3] [1, 22222, 3] #a值不变,c的第二个值变了，这就是copy和‘==’的不同

# 深拷贝
# deepcopy对外围和内部元素都进行了拷贝对象本身，而不是对象的引用。

#copy.copy()

a=[1,2,[3,4]]  #第三个值为列表[3,4],即内部元素
d=copy.copy(a) #浅拷贝a中的[3，4]内部元素的引用，非内部元素对象的本身
id(a)==id(d)
# False
id(a[2])==id(d[2])
# True
a[2][0]=3333  #改变a中内部原属列表中的第一个值
print(d)             #这时d中的列表元素也会被改变
# [1, 2, [3333, 4]]

#copy.deepcopy()

e=copy.deepcopy(a) #e为深拷贝了a
a[2][0]=333 #改变a中内部元素列表第一个的值
print(e)
# [1, 2, [3333, 4]] #因为时深拷贝，这时e中内部元素[]列表的值不会因为a中的值改变而改变

