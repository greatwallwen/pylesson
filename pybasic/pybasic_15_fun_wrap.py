'''
装饰器，这一节采用第一种讲解方式
'''
# 讲 Python 装饰器前，我想先举个例子，虽有点污，但跟装饰器这个话题很贴切。
# 夏天我们都穿的是沙滩裤，但是到了冬天它没法为我们防风御寒，咋办？
# 我们想到的一个办法就是把沙滩裤改造一下，让它变得更厚更长，这样一来，它不仅有遮羞功能，还能提供保暖。
# 不过有个问题，这个内裤被我们改造成了长裤后，虽然还有遮羞功能，但本质上它不再是一条真正的内裤了。
# 于是聪明的人们发明长裤，直接把长裤套在了沙滩裤外面，这样有了长裤后再也不冷了。
# 装饰器就像我们这里说的长裤，在不影响沙滩裤作用的前提下，给我们的身子提供了保暖的功效。
# 谈装饰器前，还要先要明白一件事，Python 中的函数和 Java、C++不太一样，
# Python 中的函数可以像普通变量一样当做参数传递给另外一个函数，例如：
import logging
from urllib import request


def foo():
    print("foo")

def bar(func):
    func()

bar(foo)
# 正式回到我们的主题。装饰器本质上是一个 Python 函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下
# 增加额外功能，装饰器的返回值也是一个函数/类对象。它经常用于有切面需求的场景，
# 比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计。
# 有了装饰器，我们就可以抽离出大量与函数功能本身无关的雷同代码到装饰器中并继续重用。
# 概括的讲，装饰器的作用就是为已经存在的对象添加额外的功能。
# 先来看一个简单例子，虽然实际代码可能比这复杂很多：
def foo():
    print('i am foo')
# 现在有一个新的需求，希望可以记录下函数的执行日志，于是在代码中添加日志代码：
def foo():
    print('i am foo')
    logging.info("foo is running")
# 如果函数 bar()、bar2() 也有类似的需求，怎么做？再写一个 logging 在 bar 函数里？
# 这样就造成大量雷同的代码，为了减少重复写代码，我们可以这样做，
# 重新定义一个新的函数：专门处理日志 ，日志处理完之后再执行真正的业务代码
def use_logging(func):
    logging.warning("%s is running" % func.__name__)
    func()

def foo():
    print('i am foo')

use_logging(foo)
# 这样做逻辑上是没问题的，功能是实现了，但是我们调用的时候不再是调用真正的业务逻辑 foo 函数，
# 而是换成了 use_logging 函数，这就破坏了原有的代码结构，
# 现在我们不得不每次都要把原来的那个 foo 函数作为参数传递给 use_logging 函数，
# 那么有没有更好的方式的呢？当然有，答案就是装饰器。
'''
简单装饰器
'''
def use_logging(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()   # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
    return wrapper

def foo():
    print('i am foo')

foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，
# 这条语句相当于  foo = wrapper
foo()                   # 执行foo()就相当于执行 wrapper()
# use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，
# 看起来像 foo 被 use_logging 装饰了一样，use_logging 返回的也是一个函数，
# 这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。
# @ 语法糖
# 如果你接触 Python 有一段时间了的话，想必你对 @ 符号一定不陌生了，
# 没错 @ 符号就是装饰器的语法糖，它放在函数开始定义的地方，
# 这样就可以省略最后一步再次赋值的操作。
def use_logging(func):

    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()
    return wrapper

@use_logging
def foo():
    print("i am foo")
foo()

# 如上所示，有了 @ ，我们就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。
# 你们看到了没有，foo() 函数不需要做任何修改，只需在定义的地方加上装饰器，调用的时候还是和以前一样，
# 如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，而不用重复修改函数或者增加新的封装。
# 这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。
# 装饰器在 Python 使用如此方便都要归因于 Python 的函数能像普通的对象一样能作为参数传递给其他函数，
# 可以被赋值给其他变量，可以作为返回值，可以被定义在另外一个函数内。

'''*args、**kwargs
可能有人问，如果我的业务逻辑函数 foo 需要参数怎么办？比如：
'''

# 我们可以在定义 wrapper 函数的时候指定参数：
def use_logging(func):

    def wrapper(name):
        logging.warning("%s is running" % func.__name__)
        return func(name)
    return wrapper

@use_logging
def foo(name):
    print("i am %s" % name)
foo("Alvin")
# 这样 foo 函数定义的参数就可以定义在 wrapper 函数中。
# 这时，又有人要问了，如果 foo 函数接收两个参数呢？三个参数呢？
# 更有甚者，我可能传很多个。
# 当装饰器不知道 foo 到底有多少个参数时，我们可以用 *args 来代替：

def use_logging(func):

    def wrapper(*args):
        logging.warning("%s is running" % func.__name__)
        return func(*args)
    return wrapper
# 如此一来，甭管 foo 定义了多少个参数，我都可以完整地传递到 func 中去。
# 这样就不影响 foo 的业务逻辑了。这时还有读者会问，如果 foo 函数还定义了一些关键字参数呢？比如：
def foo(name, age=None, height=None):
    print("I am %s, age %s, height %s" % (name, age, height))
foo("Alvin")
# 这时，你就可以把 wrapper 函数指定关键字函数：

def use_logging(func):

    def wrapper(*args, **kwargs):
        logging.warning("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

'''
带参数的装饰器
装饰器还有更大的灵活性，例如带参数的装饰器，在上面的装饰器调用中，该装饰器接收唯一的参数就是执行业务的函数 foo 。
装饰器的语法允许我们在调用时，提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。
比如，我们可以在装饰器中指定日志的等级，因为不同业务函数可能需要的日志级别是不一样的。
'''
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            elif level == "info":
                logging.info("%s is running" % func.__name__)
            return func(*args)
        return wrapper

    return decorator

@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)

foo()
# 上面的 use_logging 是允许带参数的装饰器。
# 它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。
# 我们可以将它理解为一个含有参数的闭包。
# 当我 们使用@use_logging(level="warn")调用的时候，Python 能够发现这一层的封装，
# 并把参数传递到装饰器的环境中。
# @use_logging(level="warn") #等价于 @decorator

# 类装饰器:在面向对象中会详细讲解

# 装饰器顺序
# 一个函数还可以同时定义多个装饰器，比如：
# @a
# @b
# @c
# def f ():
#     pass
# # 它的执行顺序是从里到外，最先调用最里层的装饰器，最后调用最外层的装饰器，它等效于
# f = a(b(c(f)))
'''
函数装饰器，这一节是一个难点，我们将分成几个部分逐步讲解
第二种讲解方式
'''
#第一步： 一切皆对象,首先来创建一个的函数:

def hi(name="njcit"):
    return "hi " + name
print(hi())
# output: 'hi njcit'

# 我们甚至可以将一个函数赋值给一个变量，比如
greet = hi
# 我们这里没有在使用小括号，因为我们并不是在调用hi函数
# 而是在将它放在greet变量里头。我们尝试运行下这个

print(greet())
# output: 'hi njcit'

# 如果我们删掉旧的hi函数，看看会发生什么！
del hi
# print(hi())
# outputs: NameError

# 第二步：在函数中定义函数
# 刚才那些就是函数的基本知识了。
# 我们来让你的知识更进一步。在Python中我们可以在一个函数中定义另一个函数：

def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")


hi()
# output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# 上面展示了无论何时你调用hi(), greet()和welcome()将会同时被调用。
# 然后greet()和welcome()函数在hi()函数之外是不能访问的，比如：

greet()
# outputs: NameError: name 'greet' is not defined

# 第三步： 从函数中返回函数
# 其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome


a = hi()
print(a)
# outputs: <function greet at 0x7f2143c01500>

# 上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
# 现在试试这个

print(a())
# outputs: now you are in the greet() function
# 再次看看这个代码。在 if/else 语句中我们返回 greet 和 welcome，而不是 greet() 和 welcome()。
# 为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；
# 然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。
# 当我们写下 a = hi()，hi() 会被执行，而由于 name 参数默认是 yasoob，所以函数 greet 被返回了。
# 如果我们把语句改为 a = hi(name = "ali")，那么 welcome 函数将被返回。
# 我们还可以打印出 hi()()，这会输出 now you are in the greet() function。

# 第四步：将函数作为参数传给另一个函数
def hi():
    return "hi njcit!"


def doSomethingBeforeHi(func):
    print("I am doing some boring work before executing hi()")
    print(func())


doSomethingBeforeHi(hi)
# outputs:I am doing some boring work before executing hi()
#        hi njcit!
# 现在你已经具备所有必需知识，来进一步学习装饰器真正是什么了。装饰器让你在一个函数的前后去执行代码。


# 第五步：你的第一个装饰器
# 在上一个例子里，其实我们已经创建了一个装饰器！现在我们修改下上一个装饰器，并编写一个稍微更有用点的程序：

def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
# outputs: "I am the function which needs some decoration to remove my foul smell"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# now a_function_requiring_decoration is wrapped by wrapTheFunction()

a_function_requiring_decoration()
# outputs:I am doing some boring work before executing a_func()
#        I am the function which needs some decoration to remove my foul smell
#        I am doing some boring work after executing a_func()

# 我们刚刚应用了之前学习到的原理。这正是 python 中装饰器做的事情！
# 它们封装一个函数，并且用这样或者那样的方式来修改它的行为。
# 现在你也许疑惑，我们在代码里并没有使用 @ 符号？那只是一个简短的方式来生成一个被装饰的函数。
# 这里是我们如何使用 @ 来运行之前的代码：

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")

a_function_requiring_decoration()
# outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

# the @a_new_decorator is just a short way of saying:
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

# 希望你现在对Python装饰器的工作原理有一个基本的理解。
# 如果我们运行如下代码会存在一个问题：
print(a_function_requiring_decoration.__name__)
# Output: wrapTheFunction
# 这并不是我们想要的！Ouput输出应该是
# "a_function_requiring_decoration"。这里的函数被warpTheFunction替代了。
# 它重写了我们函数的名字和注释文档(docstring)。
# 幸运的是Python提供给我们一个简单的函数来解决这个问题，那就是functools.wraps。
# 我们修改上一个例子来使用functools.wraps：
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration

# 第六步：蓝本规范
from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated


@decorator_name
def func():
    return ("Function is running")


can_run = True
print(func())
# Output: Function is running

can_run = False
print(func())
# Output: Function will not run
# 注意：
# @wraps接受一个函数来进行装饰，并加入了复制函数名称、注释文档、参数列表等等的功能。
# 这可以让我们在装饰器里面访问在装饰之前的函数的属性。

'''
使用场景
现在我们来看一下装饰器在哪些地方特别耀眼，以及使用它可以让一些事情管理起来变得更简单。
'''
# 授权(Authorization)
# 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)。
# 它们被大量使用于Flask和Django web框架中。这里是一个例子来使用基于装饰器的授权：
from functools import wraps


def check_auth(username, password):
    return True
def authenticate():
    pass

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)

    return decorated


# 日志(Logging)
# 日志是装饰器运用的另一个亮点。这是个例子：
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
# Output: addition_func was called

'''带参数的装饰器
来想想这个问题，难道 @ wraps不也是个装饰器吗？
但是，它接收一个参数，就像任何普通的函数能做的那样。
那么，为什么我们不也那样做呢？ 这是因为，当你使用 @ my_decorator语法时，你是在应用一个以单个函数作为参数的一个包裹函数。
记住，Python里每个东西都是一个对象，而且这包括函数！
记住了这些，我们可以编写一下能返回一个包裹函数的函数。
在函数中嵌入装饰器
我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。
'''
from functools import wraps


def logit(logfile='myfile/myfun1.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)

        return wrapped_function

    return logging_decorator


@logit()
def myfunc1():
    pass


myfunc1()


# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='myfile/myfunc2.log')
def myfunc2():
    pass


myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串