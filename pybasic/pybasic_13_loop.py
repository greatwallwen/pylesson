'''
循环输出数字，并判断大小：
实例
# !/usr/bin/python3
'''
count = 0
while count < 5:
    print(count, " 小于 5")
    count = count + 1
else:
    print(count, " 大于或等于 5")

'''
for
'''
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

'''
range()函数
'''
for i in range(-10, -100, -30):
    print(i)

'''
break and continue
'''
# while 中使用 break：
# 实例
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')

# while 中使用 continue：
# 实例
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')

'''
pass
'''
for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

# pass只是为了防止语法错误。
a=2
if a>1:
    pass #如果没有内容，可以先写pass，但是如果不写pass，就会语法错误

'''
使用内置 enumerate 函数进行遍历:
'''
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print(i, j)
