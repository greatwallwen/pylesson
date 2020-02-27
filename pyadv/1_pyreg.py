'''
re.match函数
'''
import re
print(re.match('www', 'www.runoob.com').span())  #返回元组
print(re.match('www', 'www.runoob.com').group()) #以str形式返回对象中match的元素
print(re.match('www', 'www.runoob.com').start()) #返回开始位置
print(re.match('www', 'www.runoob.com').end())   #返回结束位置
print(re.match('com', 'www.runoob.com'))  #返回元组

#第二个例子
line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# ?代表单个字符
# 修饰符	描述
# re.I	使匹配对大小写不敏感
# re.L	做本地化识别（locale-aware）匹配
# re.M	多行匹配，影响 ^ 和 $
# re.S	使 . 匹配包括换行在内的所有字符
# re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
# re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))

else:
    print("No match!!")

# re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
# 函数语法：
# re.search(pattern, string, flags=0)
print(re.search('www', 'www.runoob.com').span())
print(re.search('com', 'www.runoob.com').span()) #用match就会找不到，search就可以

'''
match和search的区别
'''
line = "Cats are smarter than dogs";

matchObj = re.match(r'dogs', line, re.M | re.I)
if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")

'''
检索和替换
'''
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)

'''
repl 参数是一个函数
'''
# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

'''
compile 函数
'''
# 当匹配成功时返回一个 Match 对象，其中：
# group([group1, …]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
# start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
# end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
# span([group]) 方法返回 (start(group), end(group))。
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four')        # 查找头部，没有匹配
print( m )
#None
m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
print( m )
#None
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
print( m )                                        # 返回一个 Match 对象
#<_sre.SRE_Match object at 0x10a42aac0>
print(m.group(0))   # 可省略 0
#'12'
print(m.start(0))   # 可省略 0
#3
print(m.end(0))     # 可省略 0
#
print(m.span(0))    # 可省略 0
#(3, 5)

#在看一个在终端运行的例子
# >>>import re
# >>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)   # re.I 表示忽略大小写
# >>> m = pattern.match('Hello World Wide Web')
# >>> print( m )                            # 匹配成功，返回一个 Match 对象
# <_sre.SRE_Match object at 0x10bea83e8>
# >>> m.group(0)                            # 返回匹配成功的整个子串
# 'Hello World'
# >>> m.span(0)                             # 返回匹配成功的整个子串的索引
# (0, 11)
# >>> m.group(1)                            # 返回第一个分组匹配成功的子串
# 'Hello'
# >>> m.span(1)                             # 返回第一个分组匹配成功的子串的索引
# (0, 5)
# >>> m.group(2)                            # 返回第二个分组匹配成功的子串
# 'World'
# >>> m.span(2)                             # 返回第二个分组匹配成功的子串索引
# (6, 11)
# >>> m.groups()                            # 等价于 (m.group(1), m.group(2), ...)
# ('Hello', 'World')
# >>> m.group(3)                            # 不存在第三个分组
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: no such group

'''
findall
'''
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

'''
re.finditer
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
re.finditer(pattern, string, flags=0)
'''
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group() )
'''
re.split
split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
'''
# >> > re.split('\W+', 'runoob, runoob, runoob.')
# ['runoob', 'runoob', 'runoob', '']
# >> > re.split('(\W+)', ' runoob, runoob, runoob.')
# ['', ' ', 'runoob', ', ', 'runoob', ', ', 'runoob', '.', '']
# >> > re.split('\W+', ' runoob, runoob, runoob.', 1)
# ['', 'runoob, runoob, runoob.']
#
# >> > re.split('a*', 'hello world')  # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
# ['hello world']