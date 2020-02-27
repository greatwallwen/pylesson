#!/usr/bin/env python
# coding: utf-8

'''
数据清洗
'''
# 空值和缺失值的处理 ###

from pandas import DataFrame, Series
import pandas as pd
from numpy import NaN
import numpy as np

series_obj = Series([1, None, NaN])
pd.isnull(series_obj)       # 检查是否为空值或缺失值

series_obj = Series([1, None, NaN])
pd.notnull(series_obj)       # 检查是否不为空值或缺失值

df_obj = pd.DataFrame({"类别":['小说', '散文随笔', '青春文学', '传记'],
                       "书名":[np.nan, '《皮囊》', '《旅程结束时》', '《老舍自传》'],
                       "作者":["老舍", None, "张其鑫", "老舍"]})
df_obj

df_obj.dropna()     # 删除数据集中的空值和缺失值

df_obj = pd.DataFrame({'A': [1, 2, 3, NaN],
                       'B': [NaN, 4, NaN, 6],
                       'C': ['a', 7, 8, 9],
                       'D':[NaN, 2, 3, NaN]})
df_obj

df_obj.fillna('66.0')   # 使用66替换缺失值

df_obj = pd.DataFrame({'A': [1, 2, 3, NaN],
                       'B': [NaN, 4, NaN, 6],
                       'C': ['a', 7, 8, 9],
                       'D': [NaN, 2, 3, NaN]})
df_obj


df_obj.fillna({'A': 4.0, 'B': 5.0})  # 指定列填充数据

df = pd.DataFrame({'A': [1, 2, 3, None],
                   'B': [NaN, 4, None, 6],
                   'C': ['a', 7, 8, 9],
                   'D': [None, 2, 3, NaN]})
df

df.fillna(method='ffill')   # 使用前向填充的方式替换空值或缺失值

'''
重复值的处理 ###
'''

person_info = pd.DataFrame({'id': [1, 2, 3, 4, 4, 5],
                            'name': ['小铭', '小月月', '彭岩', '刘华', '刘华', '周华'],
                            'age': [18, 18, 29, 58, 58, 36],
                            'height': [180, 180, 185, 175, 175, 178],
                            'gender': ['女', '女', '男', '男', '男', '男']})
person_info.duplicated()         # 从前向后查找和判断是否有重复值


person_info = pd.DataFrame({'id': [1, 2, 3, 4, 4, 5],
                            'name': ['小铭', '小月月', '彭岩', '刘华', '刘华', '周华'],
                            'age': [18, 18, 29, 58, 58, 36],
                            'height': [180, 180, 185, 175, 175, 178],
                            'gender': ['女', '女', '男', '男', '男', '男']})
person_info. drop_duplicates()


# ### 异常值的处理 ###

# ser1 表示传入DataFrame的某一列
def three_sigma(ser1):
    # 求平均值
    mean_value = ser1.mean()
    # 求标准差
    std_value = ser1.std()
    # 位于(μ-3σ,μ+3σ)区间的数据是正常的，不在这个区间的数据为异常的
    # ser1中的数值小于μ-3σ或大于μ+3σ均为异常值
    # 一旦发现有异常值，就标注为True，否则标注为False
    rule = (mean_value - 3 * std_value > ser1) | (ser1.mean() + 3 * ser1.std() < ser1)
    # 返回异常值的位置索引
    index = np.arange(ser1.shape[0])[rule]
    # 获取异常数据
    outrange = ser1.iloc[index]
    return outrange

# 导入需要使用的包
file = open('../mydata/3_example_data.csv')
df = pd.read_csv(file)
df

three_sigma(df['A'])

three_sigma(df['B'])

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [2, 3, 5, 2],
                   'C': [1, 4, 7, 4],
                   'D': [1, 5, 30, 3]})
df.boxplot(column=['A', 'B', 'C', 'D'])

df = pd.DataFrame ({'菜谱名': ['红烧肉', '铁板鱿鱼',
                    '小炒肉', '干锅鸭掌', '酸菜鱼'],
                    '价格': [38, 25, 26, 388, 35]})
df.replace(to_replace=388,value=38.8)


'''
更改数据类型 ###
'''
df = pd.DataFrame({'A':['5', '6', '7'], 'B':['3', '2', '1']})
df.dtypes  # 查看数据的类型


# 创建DataFrame对象，数据的类型为int
df = pd.DataFrame({'A': ['5', '6', '7'], 'B': ['3', '2', '1']},
                  dtype='int')
df.dtypes


df = pd.DataFrame({'A': ['1', '1.2', '4.2'],
                   'B': ['-9', '70', '88'],
                   'C': ['x', '5.0', '0']})
df.dtypes


df['B'].astype(dtype='int')  # 强制转换为int类型


ser_obj = pd.Series(['1', '1.2', '4.2'])
ser_obj


# 转换object类型为float类型
pd.to_numeric(ser_obj, errors='raise')


'''
数据合并 
轴向堆叠数据 
'''

df1 = pd.DataFrame({'A': ['A0', 'A0', 'A1'],
                    'B': ['B0', 'B0', 'B1']})
df2 = pd.DataFrame({'C': ['C0', 'C0', 'C1', 'C3'],
                    'D': ['D0', 'D2', 'D2', 'D3']})
# 横向堆叠合并df1和df2，采用外连接的方式
pd.concat([df1, df2], join='outer', axis=1)


first = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2'],
                      'C': ['C0', 'C1', 'C2']})
second = pd.DataFrame({'B': ['B3', 'B4', 'B5'],
                       'C': ['C3', 'C4', 'C5'],
                       'D': ['D3', 'D4', 'D5']})
pd.concat([first, second], join='inner', axis=0)


'''
主键合并数据
'''

left = pd.DataFrame({'key':['K0','K1','K2'],
                       'A':['A0','A1','A2'],
                        'B':['B0','B1','B2']})
right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                         'C':['C0','C1','C2','C3'],
                         'D':['D0','D1','D2','D3']})
pd.merge(left, right, on='key')


left = pd.DataFrame({'key':['K0','K1','K2'],
                       'A':['A0','A1','A2'],
                       'B':['B0','B1','B2']})
right = pd.DataFrame({'key':['K0','K5','K2','K4'],
                         'B':['B0','B1','B2','B5'],
                         'C':['C0','C1','C2','C3'],
                         'D':['D0','D1','D2','D3']})
pd.merge(left, right, on=['key', 'B'])


left = pd.DataFrame({'A':['A0','A1','A2'],
                       'B':['B0','B1','B2']})
right = pd.DataFrame({'C':['C0','C1','C2'],
                         'D':['D0','D1','D2']})
pd.merge(left,right,how='outer',left_index=True,right_index=True)


'''
根据索引合并数据 ###
'''
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2']})
right = pd.DataFrame({'C': ['C0', 'C1', 'C2'],
                         'D': ['D0', 'D1', 'D2']},
                        index=[ 'a','b','c'])
left.join(right, how='outer')


left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                        'B': ['B0', 'B1', 'B2'],
                      'key': ['K0', 'K1', 'K2']})
right = pd.DataFrame({'C': ['C0', 'C1','C2'],
                         'D': ['D0', 'D1','D2']},
                        index=['K0', 'K1','K2'])
# on参数指定连接的列名
left.join(right, how='left', on='key')


'''
合并重叠数据 
'''

left = pd.DataFrame({'A': [np.nan, 'A1', 'A2', 'A3'],
                        'B': [np.nan, 'B1', np.nan, 'B3'],
                        'key': ['K0', 'K1', 'K2', 'K3']})
right = pd.DataFrame({'A': ['C0', 'C1','C2'],
                         'B': ['D0', 'D1','D2']},
                         index=[1,0,2])
# 用right的数据填充left缺失的部分
left.combine_first(right)


'''
数据重塑 
重塑层次化索引 
'''

df = pd.DataFrame({'A':['A0','A1','A2'],
                 'B':['B0','B1','B2']})
# 将df进行重塑
result = df.stack()
result

type(result)

df = pd.DataFrame({'A':['A0','A1','A2'],
                      'B':['B0','B1','B2']})
res = df.stack()  #　将df重塑为Series对象
res.unstack()      #　将Series对象转换成df


df = pd.DataFrame(np.array([[26,20,22,26],[30,25,24,20]]),
                   index=['男生人数','女生人数'],
                   columns=[['一楼','一楼','二楼','二楼'],
                              ['A教室','B教室','A教室','B教室']])
df.stack()

df.stack(level=0)   # 旋转外层索引


'''
轴向旋转
'''

df =  pd.DataFrame({'商品名称': ['荣耀9青春版','小米6x','OPPO A1',
                   '荣耀9青春版','小米6x','OPPO A1'],
                   '出售日期': ['2017年5月25日', '2017年5月25日',
                   '2017年5月25日','2017年6月18日',
                   '2017年6月18日', '2017年6月18日'],
                   '价格': ['999元', '1399元', '1399元',
                   '800元', '1200元', '1250元']})
df.pivot(index='出售日期', columns='商品名称', values='价格')

'''
转换数据 
重命名轴索引
'''

df = pd.DataFrame({'A':['A0', 'A1', 'A2', 'A3'],
                 'B':['B0', 'B1', 'B2', 'B3'],
                 'C':['C0', 'C1', 'C2', 'C3']})
df

# 重命名列索引的名称，并且在原有数据上进行修改
df.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace=True)
df


df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                   'B': ['B0', 'B1', 'B2', 'B3'],
                   'C': ['C0', 'C1', 'C2', 'C3']})
df.rename(str.lower, axis='columns')

df = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3']})
df.rename(index={1: 'a', 2: 'b'}, inplace=True)
df

'''
离散化连续数据 
'''

# 使用pandas的cut函数划分年龄组
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 32]
bins = [0, 18, 25, 35, 60, 100]
cuts = pd.cut(ages, bins)
cuts


pd.cut(ages, bins=bins, right=False)


'''
哑变量处理类别型数据 
'''

df1 = pd.DataFrame({'职业': ['工人', '学生', '司机', '教师', '导游']})
pd.get_dummies(df1, prefix=['col'])  # 哑变量处理


'''
案例—预处理部分地区信息 ##
功能实现 ###
'''
# 读取北京地区信息
file_path_bj = open('../mydata/北京地区信息.csv')
file_data_bjinfo = pd.read_csv(file_path_bj)
file_data_bjinfo

# 读取天津地区信息
file_path_tj = open('C:/Users/admin/Desktop/天津地区信息.csv')
file_data_tjinfo = pd.read_csv(file_path_tj)
file_data_tjinfo


# 检测file_data_bjinfo中的数据，返回True的表示是重复数据
file_data_bjinfo.duplicated()

# 检测file_data_tjinfo中的数据，返回True的表示是重复数据
file_data_tjinfo.duplicated()

# 北京地区 删除重复数据
file_data_bjinfo = file_data_bjinfo.drop_duplicates()
file_data_bjinfo


file_data_tjinfo.isnull() # 检测数据是否存在缺失数据


# 计算常住人口的平均数，设置为float类型并保留两位小数
population = float("{:.2f}".format(file_data_tjinfo['常住人口（万人）'].mean()))
# 以字典映射的形式将需要填充的数据进行对应
values={'常住人口（万人）':population}
file_data_tjinfo = file_data_tjinfo.fillna(value=values)
file_data_tjinfo


# 对北京地区信息进行异常值检测
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
file_data_bjinfo.boxplot(column=['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）','常住人口（万人）'])

# 对天津地区信息进行异常值检测
file_data_tjinfo.boxplot(column=['行政面积（K㎡）','户籍人口（万人）','男性','女性','GDP（亿元）','常住人口（万人）'])

# 对两地信息数据进行合并
pd.concat([file_data_bjinfo,file_data_tjinfo],ignore_index=True)
