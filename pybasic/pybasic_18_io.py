'''
输出格式美化
'''
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))


for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 注意：在第一个例子中, 每列间的空格由 print() 添加。
# 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
# 另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：
# >>> '12'.zfill(5)
# '00012'
# >>> '-3.14'.zfill(7)
# '-003.14'
# >>> '3.14159265359'.zfill(5)
# '3.14159265359'

'''
str.format() 的基本使用如下:
'''
print('{}网址： "{}!"'.format('python教程', 'www.njcit.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
# !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
import math
print('常量 PI 的值近似为： {}。'.format(math.pi))
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
import math
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
# 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ==> {1:10d}'.format(name, number))
# 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
# 最简单的就是传入一个字典, 然后使用方括号 [] 来访问键值 :
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
# 也可以通过在 table 变量前使用 ** 来实现相同的功能：
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
'''
读取键盘输入
Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
input 可以接收一个Python表达式作为输入，并将运算结果返回。
'''
mystr = input("请输入：");
print ("你输入的内容是: ", mystr)

'''
读和写文件
'''
# 打开一个文件
f = open("myfile/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()

# $ cat myfile/foo.txt
# Python 是一个非常好的语言。
# 是的，的确非常好!!

# f.read(),readline.readlines打开一个文件
f = open("myfile/foo.txt", "r")
mystr = f.read()
print(mystr)

mystr = f.readline()
print(mystr)

mystr = f.readlines()
print(mystr)

#迭代式
for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

# f.write()
# 打开一个文件
f = open("myfile/wfoo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
val = ('www.runoob.com', 14)
s = str(val)
f.write(s)
# $ cat myfile/wfoo.txt
# ('www.runoob.com', 14)
# 关闭打开的文件
f.close()

# f.tell()
# f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
# f.seek()
# 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
# from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
# seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
# seek(x,1) ： 表示从当前位置往后移动x个字符
# seek(-x,2)：表示从文件的结尾往前移动x个字符
# from_what 值为默认为0，即文件开头。下面给出一个完整的例子：
# f = open("myfile/wfoo.txt", 'rb+')
# >>> f.write(b'0123456789abcdef')
# 16
# >>> f.seek(5)     # 移动到文件的第六个字节
# 5
# >>> f.read(1)
# b'5'
# >>> f.seek(-3, 2) # 移动到文件的倒数第三字节
# 13
# >>> f.read(1)
# b'd'

'''
pickle 模块
'''
#!/usr/bin/python3
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open("myfile/data.pkl", 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()

# 实例 2
# #!/usr/bin/python3
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open("myfile/data.pkl", 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

'''
python文件写入也可以进行网站爬虫
以下代码是打开baidusite.txt文件，并向里面写入http://www.baidu.com网站代码。
'''
from urllib import request
response = request.urlopen("http://www.baidu.com/")  # 打开网站
fi = open("myfile/baidusite.txt", 'w')                        # open一个txt文件
page = fi.write(str(response.read()))                # 网站代码写入
fi.close()                                           # 关闭txt文件