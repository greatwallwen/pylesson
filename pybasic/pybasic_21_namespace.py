'''
生命周期ß
'''
# var1 是全局名称
var1 = 5

def some_func():
    # var2 是局部名称
    var2 = 6

    def some_inner_func():
        # var3 是内嵌的局部名称
        var3 = 7

# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这些语句内定义的变量，外部也可以访问，如下代码：
# >>> if True:
# ...  msg = 'I am from Runoob'
# ...
# >>> msg
# 'I am from Runoob'
# >>>
# 实例中 msg 变量定义在 if 语句块中，但外部还是可以访问的。
# 如果将 msg 定义在函数中，则它就是局部变量，外部不能访问：
# >>> def test():
# ...     msg_inner = 'I am from Runoob'
# ...
# >>> msg_inner
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'msg_inner' is not defined
# >>>

'''
全局变量和局部变量
'''
total = 0  # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

'''
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
'''
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

# 如果要修改嵌套作用域（enclosing作用域，外层非全局作用域）中的变量则需要nonlocal 关键字了，如下实例：

def outer():
    num = 10

    def inner():
        nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)

    inner()
    print(num)
outer()

# 另外有一种特殊情况，假设下面这段代码被运行：

a = 10

def test(): #def test(a)
    a = a + 1
    print(a)

test()  #修改为test(a),修改 a 为全局变量，通过函数参数传递。
# 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。