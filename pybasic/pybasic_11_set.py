'''
集合（set）基本操作
'''
# >> > basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# >> > print(basket)  # 这里演示的是去重功能

# >> > 'orange' in basket  # 快速判断元素是否在集合内

# >> > 'crabgrass' in basket

# >> >  # 下面展示两个集合间的运算.

# >> > a = set('abracadabra')
# >> > b = set('alacazam')
# >> > a

# >> > a - b  # 集合a中包含而集合b中不包含的元素

# >> > a | b  # 集合a或b中包含的所有元素

# >> > a & b  # 集合a和b中都包含了的元素

# >> > a ^ b  # 不同时包含于a和b的元素

# 类似列表推导式，同样集合支持集合推导式(Set comprehension):
# >>>a = {x for x in 'abracadabra' if x not in 'abc'}
# >>> a
# {'r', 'd'}

'''
add
'''
thisset1 = set(("Google", "Runoob", "Taobao"))
thisset1.add("Facebook")
print(thisset1)
thisset1.update({1, 3})
print(thisset1)

'''
移除元素
'''
thisset2 = set(("Google", "Runoob", "Taobao"))
thisset2.remove("Taobao")
print(thisset2)
# thisset.remove("Facebook")   # 不存在会发生错误
thisset2.discard("Google")
print(thisset2)

'''
计算和清空
'''
print(len(thisset2))
thisset2.clear()
print(thisset2)

'''

'''
thisset3 = set(("Google", "Runoob", "Taobao"))
if "Runoob" in thisset3:
    print("True")
else:
    print("False")
if "Facebook" in thisset3:
    print("True")
else:
    print("False")

'''
s.update( "字符串" ) 与 s.update( {"字符串"} ) 含义不同:
 s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
 s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
'''
thisset3 = set(("Google", "Runoob", "Taobao"))
print(thisset3)
thisset3.update({"Facebook"})
print(thisset3)
thisset3.update("Yahoo")
print(thisset3)

'''
set() 中参数注意事项
'''
# 1.创建一个含有一个元素的集合
thisset4 = set(('apple',))
print(thisset4)
thisset5 = set(('apple'))
print(thisset5)




