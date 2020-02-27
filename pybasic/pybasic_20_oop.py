'''
类对象
'''
# !/usr/bin/python3
import functools


class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

# 类有一个名为__init__()的特殊方法（构造方法），该方法在类实例化时会自动调用，像下面这样：

# def __init__(self):
#     self.data = []

# 类定义了__init__()方法，类的实例化操作会自动调用__init__()方法。
# 如下实例化类MyClass，对应的__init__()方法就会被调用:
# x = MyClass()
# 当然， __init__()方法可以有参数，参数通过__init__()传递到类的实例化操作上。

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5

# self代表类的实例，而非类类的方法与普通的函数只有一个特别的区别——
# 它们必须有一个额外的第一个参数名称, 按照惯例它的名称是self。

class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
# 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的:

'''
类的方法，在类的内部，使用
'''
# def 关键字来定义一个方法，
# 与一般函数定义不同，类方法必须包含参数self, 且为第一个参数，self代表的是类的实例。
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()

'''
继承
'''
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()

'''
多继承
'''


# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class speaker():
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

'''
方法重写
'''
class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法

'''
类属性与方法
'''


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
# print(counter.__secretCount)  # 报错，实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('python教程', 'www.njcit.cn')
x.who()  # 正常输出
x.foo()  # 正常输出
# x.__foo()  # 报错

'''
运算符重载
'''

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

'''
Python3 中类的静态方法、普通方法、类方法
静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。
普通方法: 默认有个self参数，且只能被对象调用。
类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。
'''
class Classname:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')



Classname.fun()
Classname.a()

C = Classname()
C.fun()
C.a()
C.b()

'''
反向运算符重载：
__radd__: 加运算
__rsub__: 减运算
__rmul__: 乘运算
__rdiv__: 除运算
__rmod__: 求余运算
__rpow__: 乘方
复合重载运算符：
__iadd__: 加运算
__isub__: 减运算
__imul__: 乘运算
__idiv__: 除运算
__imod__: 求余运算
__ipow__: 乘方
'''
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __repr__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        if other.__class__ is Vector:
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            return Vector(self.a+other,self.b)

    def __radd__(self,other):
        """反向算术运算符的重载
        __add__运算符重载可以保证V+int的情况下不会报错，但是反过来int+V就会报错，通过反向运算符重载可以解决此问题
        """
        if other.__class__ is int or other.__class__ is float:
            return Vector(self.a+other,self.b)
        else:
            raise ValueError("值错误")

    def __iadd__(self,other):
        """复合赋值算数运算符的重载
        主要用于列表，例如L1+=L2,默认情况下调用__add__，会生成一个新的列表，
        当数据过大的时候会影响效率，而此函数可以重载+=，使L2直接增加到L1后面
        """
        if other.__class__ is Vector:
            return Vector(self.a + other.a, self.b + other.b)
        elif other.__class__ is int:
            return Vector(self.a+other,self.b)
v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)
print (v1+5)
print (6+v2)


'''装饰器类
装饰器不仅可以是函数，还可以是类，相比函数装饰器，类装饰器具有灵活度大、高内聚、封装性等优点。
使用类装饰器主要依靠类的__call__方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
'''
from functools import wraps
class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')

@Foo
def bar():
    print ('bar')

bar()
functools.wraps

# 使用装饰器极大地复用了代码，但是他有一个缺点就是原函数的元信息不见了，
# 比如函数的docstring、__name__、参数列表，先看例子：
def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)    # 输出 'with_logging'
        print(func.__doc__)     # 输出 None
        return func(*args, **kwargs)
    return with_logging

# 函数
@logged
def f(x):
   """does some math"""
   return x + x * x

logged(f)
# 不难发现，函数 f 被with_logging取代了，当然它的docstring，__name__就是变成了with_logging函数的信息了。
# 好在我们有functools.wraps，wraps本身也是一个装饰器，
# 它能把原函数的元信息拷贝到装饰器里面的 func 函数中，
# 这使得装饰器里面的 func 函数也有和原函数 foo 一样的元信息了。
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__)      # 输出 'f'
        print(func.__doc__)      # 输出 'does some math'
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

# 现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。
# 比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。
# 这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。
# 幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建logit。
class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass


# 这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

@logit()
def myfunc1():
    pass


# 现在，我们给logit创建子类，来添加email的功能(虽然email这个话题不会在这里展开)。

class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''

    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass


'''
后面我们都在python console中来运行程序
__slots__
'''

# 正常情况下，当我们定义了一个class，
# 创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：

class Student(object):
    pass
# 然后，尝试给实例绑定一个属性：

# s = Student()
# s.name = 'Michael' # 动态给实例绑定一个属性
# print(s.name)
# # Michael
# # 还可以尝试给实例绑定一个方法：
#
# def set_age(self, age): # 定义一个函数作为实例方法
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
# s.set_age(25) # 调用实例方法
# s.age # 测试结果
# 25
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

# >>> s2 = Student() # 创建新的实例
# >>> s2.set_age(25) # 尝试调用方法
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'set_age'
# 为了给所有实例都绑定方法，可以给class绑定方法：
#
# >>> def set_score(self, score):
# ...     self.score = score
# ...
# >>> Student.set_score = set_score
# 给class绑定方法后，所有实例均可调用：
#
# >>> s.set_score(100)
# >>> s.score
# 100
# >>> s2.set_score(99)
# >>> s2.score
# 99
# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
#
# 使用__slots__
#
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
#
# class Student(object):
#     __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
# 然后，我们试试：
#
# >>> s = Student() # 创建新的实例
# >>> s.name = 'Michael' # 绑定属性'name'
# >>> s.age = 25 # 绑定属性'age'
# >>> s.score = 99 # 绑定属性'score'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Student' object has no attribute 'score'
# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
#
# >>> class GraduateStudent(Student):
# ...     pass
# ...
# >>> g = GraduateStudent()
# >>> g.score = 9999
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

'''
使用@property
'''
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
# 但是，没办法检查参数，导致可以把成绩随便改：
#
# s = Student()
# s.score = 9999
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
#
# class Student(object):
#
#     def get_score(self):
#          return self._score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
#
# >>> s = Student()
# >>> s.set_score(60) # ok!
# >>> s.get_score()
# 60
# >>> s.set_score(9999)
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于追求完美的Python程序员来说，这是必须要做到的！
#
# 还记得装饰器（decorator）可以给函数动态加上功能吗？
# 对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
#
# class Student(object):
#
#     @property
#     def score(self):
#         return self._score
#
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，
# 于是，我们就拥有一个可控的属性操作：
#
# >>> s = Student()
# >>> s.score = 60 # OK，实际转化为s.set_score(60)
# >>> s.score # OK，实际转化为s.get_score()
# 60
# >>> s.score = 9999
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
# 注意到这个神奇的@property，我们在对实例属性操作的时候，
# 就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
#
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，
# 因为age可以根据birth和当前时间计算出来。

'''
定制类
'''
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，
# 但是，没办法检查参数，导致可以把成绩随便改：

s = Student()
s.score = 9999
# 这显然不合逻辑。为了限制score的范围，
#
# 可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：

# >>> s = Student()
# >>> s.set_score(60) # ok!
# >>> s.get_score()
# 60
# >>> s.set_score(9999)
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
#
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于追求完美的Python程序员来说，这是必须要做到的！
#
# 还记得装饰器（decorator）可以给函数动态加上功能吗？
# 对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，
# 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

# >>> s = Student()
# >>> s.score = 60 # OK，实际转化为s.set_score(60)
# >>> s.score # OK，实际转化为s.get_score()
# 60
# >>> s.score = 9999
# Traceback (most recent call last):
#   ...
# ValueError: score must between 0 ~ 100!
# 注意到这个神奇的@property，我们在对实例属性操作的时候，
# 就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
#
# class Student(object):
#
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2015 - self._birth
# 上面的birth是可读写属性，而age就是一个只读属性，
# 因为age可以根据birth和当前时间计算出来。

'''
枚举类
'''

# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：

JAN = 1
FEB = 2
MAR = 3
...
NOV = 11
DEC = 12
# 好处是简单，缺点是类型是int，并且仍然是变量。

# 更好的方法是为这样的枚举类型定义一个class类型，
# 然后，每个常量都是class的一个唯一实例。
# Python提供了Enum类来实现这个功能：

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar',
                       'Apr', 'May', 'Jun', 'Jul',
                       'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# @unique装饰器可以帮助我们检查保证没有重复值。

# 访问这些枚举类型可以有若干种方法：

# >>> day1 = Weekday.Mon
# >>> print(day1)
# Weekday.Mon
# >>> print(Weekday.Tue)
# Weekday.Tue
# >>> print(Weekday['Tue'])
# Weekday.Tue
# >>> print(Weekday.Tue.value)
# 2
# >>> print(day1 == Weekday.Mon)
# True
# >>> print(day1 == Weekday.Tue)
# False
# >>> print(Weekday(1))
# Weekday.Mon
# >>> print(day1 == Weekday(1))
# True
# >>> Weekday(7)
# Traceback (most recent call last):
#   ...
# ValueError: 7 is not a valid Weekday
# >>> for name, member in Weekday.__members__.items():
# ...     print(name, '=>', member)
# ...
# Sun => Weekday.Sun
# Mon => Weekday.Mon
# Tue => Weekday.Tue
# Wed => Weekday.Wed
# Thu => Weekday.Thu
# Fri => Weekday.Fri
# Sat => Weekday.Sat
# 可见，既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
#

'''
使用元类
'''
# type()
#
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
#
# 比方说我们要定义一个Hello的class：

# class Hello(object):
#     def hello(self, name='world'):
#         print('Hello, %s.' % name)

# 当Python解释器载入hello类时，就会依次执行该类的所有语句，
# 执行结果就是动态创建出一个Hello的class对象，我们在测试如下：

# >>> from hello import Hello
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class 'hello.Hello'>

# type()函数可以查看一个类型或变量的类型，Hello是一个class，
# 它的类型就是type，而h是一个实例，它的类型就是class Hello。

# 我们说class的定义是运行时动态创建的，
# 而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# 比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

# >>> def fn(self, name='world'): # 先定义函数
# ...     print('Hello, %s.' % name)
# ...
# >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# >>> h = Hello()
# >>> h.hello()
# Hello, world.
# >>> print(type(Hello))
# <class 'type'>
# >>> print(type(h))
# <class '__main__.Hello'>
# 要创建一个class对象，type()函数依次传入3个参数：

# class的名称；
# 继承的父类集合，注意Python支持多重继承，
# 如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，
# 因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#
# 正常情况下，我们都用class Xxx...来定义类，
# 但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，
# 或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
#
