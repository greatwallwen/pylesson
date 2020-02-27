'''
迭代器
'''
# !/usr/bin/python3

import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=" ")

# 也可以使用next()函数：


list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

while True:
    try:
        print(next(it))
    except StopIteration:
        break
        # sys.exit()

'''
创建一个迭代器
'''
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

'''
StopIteration
'''


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)

'''
生成器
'''
# 打个比方的话，yield有点像断点。     加了yield的函数，每次执行到有yield的时候，会返回yield后面的值
# 并且函数会暂停，直到下次调用或迭代终止；
# yield后面可以加多个数值（可以是任意类型），但返回的值是元组类型的。
def get():
    m = 0
    n = 2
    l = ['s', 1, 3]
    k = {1: 1, 2: 2}
    p = ('2', 's', 't')
    while True:
        m += 1
        yield m
        yield m, n, l, k, p


it = get()
print(next(it))  # 1
print(next(it))  # (1, 2, ['s', 1, 3], {1: 1, 2: 2}, ('2', 's', 't'))

print(next(it))  # 2
print(next(it))  # <class 'tuple'>


import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if counter > n:
            return
        yield a         #使用yield，和不使用yield
        a, b = b, a + b
        print('%d,%d' % (a, b))
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except:
        sys.exit()

'''
列表生成式
'''
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

# >>> list(range(1, 11))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

# >>> L = []
# >>> for x in range(1, 11):
# ...    L.append(x * x)
# ...
# >>> L
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：

# >>> [x * x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

# >>> [x * x for x in range(1, 11) if x % 2 == 0]
# [4, 16, 36, 64, 100]
# 还可以使用两层循环，可以生成全排列：
#
# >>> [m + n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 三层和三层以上的循环就很少用到了。
# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

# >>> import os # 导入os模块，模块的概念后面讲到
# >>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
# ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：

d = {'x': 'A', 'y': 'B', 'z': 'C' }
L=[k + '=' + v for k, v in d.items()]
print(l)

# ['y=B', 'x=A', 'z=C']
# 最后把一个list中所有的字符串变成小写：

L = ['Hello', 'World', 'IBM', 'Apple']
Low=[s.lower() for s in L]
print(Low)
# ['hello', 'world', 'ibm', 'apple']

'''
if ... else
'''
# 使用列表生成式的时候，有些童鞋经常搞不清楚if...else的用法。
# 例如，以下代码正常输出偶数：

L=[x for x in range(1, 11) if x % 2 == 0]
print(L)
# [2, 4, 6, 8, 10]

# 但是，我们不能在最后的if加上else：

# L=[x for x in range(1, 11) if x % 2 == 0 else 0]
# SyntaxError: invalid syntax
# 这是因为跟在for后面的if是一个筛选条件，不能带else，否则如何筛选？

# 另一些童鞋发现把if写在for前面必须加else，否则报错：

# L=[x if x % 2 == 0 for x in range(1, 11)]

# SyntaxError: invalid syntax
# 这是因为for前面的部分是一个表达式，它必须根据x计算出一个结果。
# 因此，考察表达式：x if x % 2 == 0，它无法根据x计算出结果，
# 因为缺少else，必须加上else：

L=[x if x % 2 == 0 else -x for x in range(1, 11)]
# [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
# 上述for前面的表达式x if x % 2 == 0 else -x才能根据x计算出确定的结果。
# 可见，在一个列表生成式中，for前面的if ... else是表达式，而for后面的if是过滤条件，不能带else。
'''
生成器另一种理解方法
'''
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
#
# >>> L = [x * x for x in range(3)]
# >>> L
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# >>> g = (x * x for x in range(3))
# >>> g
# <generator object <genexpr> at 0x1022ef630>

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
# 我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：

# >>> next(g)
# 0
# >>> next(g)
# 1
# >>> next(g)
# 4
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# 我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，
# 直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，
# 因为generator也是可迭代对象：

g = (x * x for x in range(10))
for n in g:
    print(n)
# 所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
# 注意，赋值语句：
# a, b = b, a + b
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]
# 但不必显式写出临时变量t就可以赋值。
# 上面的函数可以输出斐波那契数列的前N个数：

fib(6)
# 'done'
# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，
# 可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，
# 只需要把print(b)改为yield b就可以了：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：

f = fib(6)
f
# <generator object fib at 0x104feaaa0>
# 这里，最难理解的就是generator和函数的执行流程不一样。
# 函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。

# 举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
# 调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：

o = odd()
print(next(o))
# step 1
# 1
print(next(o))
# step 2
# 3
print(next(o))
# step 3
# 5
print(next(o))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
# 同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，
# 而是直接使用for循环来迭代：

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

# >>> g = fib(6)
# >>> while True:
# ...     try:
# ...         x = next(g)
# ...         print('g:', x)
# ...     except StopIteration as e:
# ...         print('Generator return value:', e.value)
# ...         break
# ...
# g: 1
# g: 1
# g: 2
# g: 3
# g: 5
# g: 8
# Generator return value: done