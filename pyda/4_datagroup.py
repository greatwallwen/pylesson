'''
数据聚合与组内运算
通过groupby()方法拆分数据
'''

import pandas as pd
df = pd.DataFrame({"Key":['C','B','C','A','B','B','A','C','A'],
                   "Data":[2,4,6,8,10,1,14,16,18]})
df

# 按Key列进行分组
df.groupby(by='Key')

group_obj = df.groupby('Key')
# 遍历分组对象
for i in group_obj:
    print(i)

import pandas as pd
import numpy as np
df = pd.DataFrame({'key1': ['A', 'A', 'B', 'B', 'A'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': [2, 3, 4, 6, 8],
                   'data2': [3, 5, 6, 3, 7]})
df

se = pd.Series(['a', 'b', 'c', 'a', 'b'])
se

# 按自定义Series对象进行分组
group_obj = df.groupby(by = se)   
for i in group_obj:                  # 遍历分组对象
    print(i)

# 当Series长度与原数据的索引值长度不同时
se = pd.Series(['a', 'a', 'b'])
group_obj = df.groupby(se)
for i in group_obj:           # 遍历分组对象
    print(i)

from pandas import DataFrame, Series
num_df = DataFrame({'a': [1, 2, 3, 4, 5],
                    'b': [6, 7, 8, 9, 10],
                    'c': [11, 12, 13, 14, 15],
                    'd': [5, 4, 3, 2, 1],
                    'e': [10, 9, 8, 7, 6]})
num_df

# 定义分组关系
mapping = {'a':'第一组','b':'第二组','c':'第一组',
           'd':'第三组','e':'第二组'}
mapping

# 按字典分组
by_column = num_df.groupby(mapping, axis=1)
for i in by_column:
    print(i)

import pandas as pd
df = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                   'b': [6, 7, 8, 9, 10],
                   'c': [5, 4, 3, 2, 1]},
                  index=['Sun', 'Jack', 'Alice', 'Helen', 'Job'])
df

groupby_obj = df.groupby(len)     # 使用内置函数len进行分组
for group in groupby_obj:        # 遍历分组对象
    print(group)

'''数据聚合
使用内置统计方法聚合数据
'''

df = pd.DataFrame({'key1': ['A', 'A', 'B', 'B', 'A'],
                   'key2': ['one', 'two', 'one', 'two', 'one'],
                   "data1": [2, 3, 4, 6, 8],
                   "data2": [3, 5, np.nan, 3,7]})
df

df.groupby('key1').mean() # 按key1进行分组，求每个分组的平均值


'''
	面向列的聚合方法（agg）
'''
data_frame = DataFrame(np.arange(36).reshape((6, 6)),
                       columns=list('abcdef'))
data_frame['key'] = Series(list('aaabbb'), name='key')
data_frame

# 按key列进行分组
data_group = data_frame.groupby('key')
# 输出a组数据信息
dict([x for x in data_group])['a']

# 输出b组数据信息
dict([x for x in data_group])['b']

# 求每个分组的和
data_group.agg(sum)

def range_data_group(arr):
    return arr.max()-arr.min()

data_group.agg(range_data_group)  # 使用自定义函数聚合分组数据

# 对一列数据用两种函数聚合
data_group.agg([range_data_group, sum])

data_group.agg([("极差", range_data_group), ("和", sum)])

# 每列使用不同的函数聚合分组数据
data_group.agg({'a': 'sum', 'b': 'mean', 'c': range_data_group})

'''
其它分组级运算
数据转型（transform）
'''

df = pd.DataFrame({'a': [0, 1, 6, 10, 3],
                   'b': [1, 2, 7, 11, 4],
                   'c': [2, 3, 8, 12, 4],
                   'd': [3, 4, 9, 13, 5],
                   'e': [4, 5, 10, 14, 3],
                   'key': ['A', 'A', 'B', 'B', 'B']})
df

data_group = df.groupby('key').transform('mean')

data_group

import pandas as pd
df = pd.DataFrame({'A': [2, 3, 3, 4, 2],
                   'B': [4, 2, 3, 6, 6],
                   'C': [9, 7, 0, 7, 8],
                   'D': [3, 4, 8, 6, 10]})
df

# 以key为分组依据，对df对象进行分组
key = ['one','one','two',' two',' two']
df.groupby(key).transform('mean')


'''
数据应用（apply）
'''
data_frame = DataFrame({'data1': [80,23,25,63,94,92,99,92,82,99],
                        'data2': [41,87,58,68,72,89,60,42,53,65],
                        'data3': [30,78,23,66,16,59,20,23,24,40],
                        'key': list('baabbabaaa')})
data_frame

# 对数据进行分组
data_by_group = data_frame.groupby('key')
# 打印分组数据
dict([x for x in data_by_group])['a']

dict([x for x in data_by_group])['b']

# 调用apply()方法聚合，求每个分组中的最大值
data_by_group.apply(max)


'''
案例—运动员信息的分组与聚合
'''
# 读取运行员信息表.csv文件中的内容
f1 = open('../mydata/运动员信息表.csv')
df = pd.read_csv(f1)
df

# 按项目一列进行分组
data_group = df.groupby('项目')
# 输出篮球分组的信息
df_basketball = dict([x for x in data_group])['篮球']
df_basketball

# 按性别一列进行分组，并使用方法
groupby_sex = df_basketball.groupby('性别')
groupby_sex.mean()

# 使用transfrom方法将数据进行聚合，并利用其特性将平均值进行广播
info = groupby_sex.transform('mean')
info

# 查看男篮运动员的分组
baseketball_male = dict([x for x in groupby_sex])['男']
baseketball_male

# 求数据极差的函数
def range_data_group(arr):
    return arr.max()-arr.min()

# 求年龄、身高、体重这三列数据的极差值
baseketball_male.agg({'年龄（岁）':range_data_group,
                      '身高(cm)':range_data_group,
                      '体重(kg)':range_data_group})

# 添加“体质指数”列
df_basketball['体质指数'] = 0
df_basketball

# 定义计算BMI值的函数
def outer(num):
    def ath_bmi(sum_bmi):
        weight = df_basketball['体重(kg)']
        height = df_basketball['身高(cm)'] 
        sum_bmi =  weight / (height/100)**2
        return num + sum_bmi
    return ath_bmi

all_bmi = df_basketball['体质指数']
df_basketball['体质指数'] = df_basketball[['体质指数']].apply(outer(all_bmi))
df_basketball

