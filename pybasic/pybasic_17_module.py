'''
import引入
'''
import sys
print('命令行参数如下:')
for i in sys.argv:
   print(i)
print('\n\nPython 路径为：', sys.path, '\n')
# 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
# 2、sys.argv 是一个包含命令行参数的列表。
# 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。

'''
生产新的文件myfib.py
'''
import myfibo

myfibo.fib(1000)
from myfibo import fib  #*
fib(500)

'''
dir
note：关于导入模块，自己写的程序，自己也可以把它保存下来，以后需要的时候导入使用.
例如下面所示。有个代码名称为 myfib.py，它的所在路径为 D:\test 下面。
那我只需要完成以下步骤就可以把它作为模块 import 到其他代码中了。
'''
# >>> impport sys
# >>> sys.path.append("/Users/alvin.zhu/PycharmProjects/pystudy")
# >>> import myfibo
# >>> dir(myfib)
# >>> a = [1, 2, 3, 4, 5]
# >>> import fibo
# >>> fib = fibo.fib
# >>> dir() # 得到一个当前模块中定义的属性列表
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
# >>> a = 5 # 建立一个新的变量 'a'
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'a', 'sys']
# >>>
# >>> del a # 删除变量名a
# >>>
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'sys']
# >>>

'''
package
'''
# import mypkg.mypkfibo
# mypkg.mypkfibo.fib(100)
fib(20)