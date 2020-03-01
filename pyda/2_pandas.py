'''

'''
import pandas as pd                       # 导入pandas库
import numpy as np
ser_obj = pd.Series([1, 2, 3, 4, 5])      # 创建Series类对象
ser_obj

# 创建Series类对象，并指定索引
ser_obj = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
ser_obj

year_data = {2001: 17.8, 2002: 20.1, 2003: 16.5}
ser_obj2 = pd.Series(year_data)   # 创建Series类对象
ser_obj2

ser_obj.index         # 获取ser_obj的索引

ser_obj.values       # 获取ser_obj的数据

ser_obj[3]            # 获取位置索引3对应的数据

ser_obj * 2


'''
DataFrame
'''
demo_arr = np.array([['a', 'b', 'c'], ['d', 'e', 'f']]) # 创建数组
df_obj = pd.DataFrame(demo_arr)    # 基于数组创建DataFrame对象
df_obj

# 创建DataFrame对象，指定列索引
df_obj = pd.DataFrame(demo_arr, columns=['No1', 'No2', 'No3'])
df_obj

element = df_obj['No2']  # 通过列索引的方式获取一列数据
element

type(element)                # 查看返回结果的类型

element = df_obj.No2  # 通过属性获取列数据
element

type(element)           # 查看返回结果的类型

df_obj['No4'] = ['g', 'h']
df_obj

del df_obj['No3']
df_obj


'''索引操作及高级索引
索引对象
'''
ser_obj = pd.Series(range(5), index=['a','b','c','d','e'])
ser_index = ser_obj.index
ser_index

# ser_index['2'] = 'cc'  # (执行时，将注释打开，便可以看到错误信息)

ser_obj1 = pd.Series(range(3), index=['a','b','c'])
ser_obj2 = pd.Series(['a','b','c'], index=ser_obj1.index)
ser_obj2.index is ser_obj1.index

'''
重置索引
'''
ser_obj = pd.Series([1, 2, 3, 4, 5], index=['c', 'd', 'a', 'b', 'e'])
ser_obj




# 重新索引
ser_obj2 = ser_obj.reindex(['a', 'b', 'c', 'd', 'e', 'f']) 
ser_obj2




# 重新索引时指定填充的缺失值
ser_obj2 = ser_obj.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value = 6)
ser_obj2

# 创建Series对象，并为其指定索引
ser_obj3 = pd.Series([1, 3, 5, 7], index=[0, 2, 4, 6])
ser_obj3

ser_obj3.reindex(range(6), method = 'ffill') # 重新索引，前向填充值

ser_obj3.reindex(range(6), method = 'bfill')# 重新索引，后向填充值# ### 3.2.3 索引操作
import pandas as pd
ser_obj = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
ser_obj[2]       # 使用索引位置获取数据

ser_obj['c']    # 使用索引名称获取数据

ser_obj[2: 4]           # 使用位置索引进行切片

ser_obj['c': 'e']      # 使用索引名称进行切片

ser_obj[[0, 2, 4]]          # 通过不连续位置索引获取数据集

ser_obj[['a', 'c', 'd']]   # 通过不连续索引名称获取数据集

ser_bool = ser_obj > 2         # 创建布尔型Series对象
ser_bool

ser_obj[ser_bool]               # 获取结果为True的数据
arr = np.arange(12).reshape(3, 4)
df_obj = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd'])
df_obj
df_obj['b']
type(df_obj['b'])
df_obj[['b', 'd']]        # 获取不连续的Series对象
df_obj[: 2]               # 使用切片获取第0~1行的数据

# 使用多个切片先通过行索引获取第0~2行的数据，再通过不连续列索引获取第b、d列的数据
df_obj[: 3][['b', 'd']]

# ### 多学一招import numpy as np

arr = np.arange(16).reshape(4, 4)
dataframe_obj = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd'])
dataframe_obj

dataframe_obj.loc[:, ["c", "a"]]
dataframe_obj.iloc[:, [2, 0]]
dataframe_obj.loc[1:2, ['b','c']]
dataframe_obj.iloc[1:3, [1, 2]]

'''
术运算与数据对齐
'''
obj_one = pd.Series(range(10, 13), index=range(3))
obj_one

obj_two = pd.Series(range(20, 25), index=range(5))
obj_two

obj_one + obj_two
obj_one.add(obj_two, fill_value = 0)   # 执行加法运算，补充缺失值


'''数据排序# 
按索引排序
'''
ser_obj = pd.Series(range(10, 15), index=[5, 3, 1, 3, 2])
ser_obj
ser_obj.sort_index()        # 按索引进行升序排列
ser_obj.sort_index(ascending = False)  # 按索引进行降序排列
import pandas as pd
import numpy as np
df_obj = pd.DataFrame(np.arange(9).reshape(3, 3), index=[4, 3, 5])
df_obj
df_obj.sort_index()                      # 按索引升序排列
df_obj.sort_index(ascending = False)     # 按索引降序排列

'''
按值排序
'''

ser_obj = pd.Series([4, np.nan, 6, np.nan, -3, 2])
ser_obj
ser_obj.sort_values()   # 按值升序排列
df_obj = pd.DataFrame([[0.4, -0.1, -0.3, 0.0], 
                       [0.2, 0.6, -0.1, -0.7],
                       [0.8, 0.6, -0.5, 0.1]])
df_obj
df_obj.sort_values(by = 2)  # 对列索引值为2的数据进行排序

'''统计计算与描述# 
常用的统计计算
'''
df_obj = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'c', 'd'])
df_obj
df_obj.sum()          # 计算每列元素的和
df_obj.max()         # 获取每列的最大值
df_obj.min(axis=1)   # 沿着横向轴，获取每行的最小值

'''
统计描述（descript）
'''
df_obj = pd.DataFrame([[12, 6, -11, 19],
                       [-1, 7, 50, 36],
                       [5, 9, 23, 28]])
df_obj
df_obj.describe()

'''
层次化索引
认识层次化索引
'''
import pandas as pd
mulitindex_series = pd.Series([15848,13472,12073.8,7813,7446,6444,15230,8269],
                              index=[['河北省','河北省','河北省','河北省',
                                      '河南省','河南省','河南省','河南省'],
                                     ['石家庄市','唐山市','邯郸市','秦皇岛市',
                                      '郑州市','开封市','洛阳市','新乡市']])
mulitindex_series


# 占地面积为增加的列索引
mulitindex_df = pd.DataFrame({'占地面积':[15848,13472,12073.8,7813,
                                   7446,6444,15230,8269]},
                          index=[['河北省','河北省','河北省','河北省',
                                  '河南省','河南省','河南省','河南省'],
                                 ['石家庄市','唐山市','邯郸市','秦皇岛市',
                                  '郑州市','开封市','洛阳市','新乡市']])
mulitindex_df

from pandas import MultiIndex
# 创建包含多个元组的列表
list_tuples = [('A','A1'), ('A','A2'), ('B','B1'),
               ('B','B2'), ('B','B3')]
# 根据元组列表创建一个MultiIndex对象
multi_index = MultiIndex.from_tuples(tuples=list_tuples, 
                                     names=[ '外层索引', '内层索引'])
multi_index
values = [[1, 2, 3], [8, 5, 7], [4, 7, 7], [5, 5, 4], [4, 9, 9]]
df_indexs = pd.DataFrame(data=values, index=multi_index)
df_indexs

# 根据列表创建一个MultiIndex对象
multi_array = MultiIndex.from_arrays(arrays =[['A', 'B', 'A', 'B', 'B'], 
                                              ['A1', 'A2', 'B1', 'B2', 'B3']],
                                     names=['外层索引','内层索引'])
multi_array


values = np.array([[1, 2, 3], [8, 5, 7], [4, 7, 7],
                   [5, 5, 4], [4, 9, 9]])
df_array = pd.DataFrame(data=values, index=multi_array)
df_array


numbers = [0, 1, 2]
colors = ['green', 'purple']
multi_product = pd.MultiIndex.from_product([numbers, colors], 
                                           names=['number', 'color'])

# 使用变量values接收DataFrame对象的值
values = np.array([[7, 5], [6, 6], [3, 1], [5, 5], [4, 5], [5, 3]])
df_product = pd.DataFrame(data=values, index=multi_product)
df_product

'''
层次化索引的操作
'''
from pandas import Series, DataFrame
ser_obj = Series([50, 60, 40, 94, 63, 101, 200, 56, 45],
                 index=[['小说', '小说', '小说',
                         '散文随笔', '散文随笔', '散文随笔',
                         '传记', '传记', '传记'],
                        ['高山上的小邮局', '失踪的总统', '绿毛水怪',
                         '皮囊', '浮生六记', '自在独行',
                         '梅西', '老舍自传', '库里传']])
ser_obj
ser_obj['小说']     # 获取所有外层索引为“小说”的数据
ser_obj[:,'自在独行']       # 获取内层索引对应的数据
ser_obj.swaplevel()               # 交换外层索引与内层索引位置


df_obj = DataFrame({'str':['a','b','d','e','f','k','d','s','l'],
                    'num':[1, 2, 4, 5, 3, 2, 6, 2, 3]},
                   index=[['A', 'A', 'A', 'C', 'C', 'C', 'B', 'B', 'B'],
                          [1, 3, 2, 3, 1, 2, 4, 5, 8]])
df_obj
df_obj.sort_index()         # 按索引排序

# 按num列降序排列
df_obj.sort_index(by='num',ascending=False)

'''
读写数据操作# ### 3.7.1 读写文本文件i
'''
df = pd.DataFrame({'one_name':[1,2,3], 'two_name':[4,5,6]})
# 将df对象写入到csv格式的文件中
df.to_csv(r'E:/数据分析/itcast.csv',index=False)
'写入完毕'

file = open(r"E:/数据分析/itcast.csv")
# 读取指定目录下的csv格式的文件
file_data = pd.read_csv(file)
file_data

file = open(r'E:/数据分析/itcast.txt')
data = pd.read_table(file)
data


'''
读写Excel文件
'''
df1 = pd.DataFrame({'col1': ['传', '智'], 'col2': ['播', '客']})
df1.to_excel(r'E:/数据分析/itcast.xlsx', 'python基础班')
'写入完毕'

excel_path =r'E:/数据分析/itcast.xlsx'
data = pd.read_excel(excel_path)
data

'''
读取HTML表格数据
'''
import requests
html_data = requests.get('http://kaoshi.edu.sina.com.cn/college/majorlist/')
html_table_data = pd.read_html(html_data.content,encoding='utf-8')
html_table_data[1]
'''
读写数据库
'''
# from pandas import DataFrame
# from sqlalchemy import create_engine
# import pandas as pd
#  # mysql账号为testuser  密码为test@123 数据名：person_info
#  # 数据表名称：person_info
# engine = create_engine('mysql+pymysqlconnector://root:test@123@localhost/TESTDB')
# pd.read_sql('person_info',engine)

import pandas as pd
import pymysql

con = pymysql.connect(host='localhost', user='testuser', password='test@123', db='testdb',
                      charset='utf8', use_unicode=True)
sql = 'SELECT * FROM person_info'
df = pd.read_sql(sql, con=con)
print(df.head())
print(df.dtypes)
con.close()



from sqlalchemy import create_engine
# 创建数据库引擎
# mysql+pymysql 表示使用Mysql数据库的pymysql驱动
engine = create_engine('mysql+pymysql://testuser:test@123@127.0.0.1/TESTDB')
sql = 'select * from person_info where id >1;'
pd.read_sql(sql,engine)


# 创建数据库引擎
# mysql+pymysql 表示使用Mysql数据库的pymysql驱动
# 账号：root 密码：123456 数据库名：studnets_info
# 数据表的名称： students

engine=create_engine('mysql+pymysql://testuser:test@123@127.0.0.1/TESTDB')
df = DataFrame({"class":["一年级","二年级","三年级","四年级"],
                              "MaleNum":[25,23,27,30],
                              "FemaleNum":[19,17,20,20]})
# df.to_sql('students',engine)
df.to_sql(name='students', con=engine,if_exists = 'append',index=False)
# name是表名
# con是连接
# if_exists：表如果存在怎么处理
# append：追加
# replace：删除原表，建立新表再添加
# fail：什么都不干
# index=False：不插入索引index
'''
案例—
读取2004-2016年的流感数据，并拼接为一个数据框；
读入人口数据，按年份和地区对流感数据填充人口数。
'''
# 指定文件的路径
file_path = '../mydata/scores.xlsx'
# 指定列标签的索引列表
df_obj = pd.read_excel(file_path, header=[0, 1])
df_obj
sorted_obj = df_obj.sort_index(ascending = False)
sorted_obj
sorted_obj.max()
sorted_obj.min()
result1 = sorted_obj["一本分数线", "文科"].to_numpy().ptp()
result1
result2 = sorted_obj["一本分数线", "理科"].to_numpy().ptp()
result2
result3 = sorted_obj["二本分数线", "文科"].to_numpy().ptp()
result3
result4 = sorted_obj["二本分数线", "理科"].to_numpy().ptp()
result4
ser_obj1 = sorted_obj['一本分数线','文科']
ser_obj1[2018] - ser_obj1[2017]
ser_obj2 = sorted_obj['一本分数线','理科']
ser_obj2[2018] - ser_obj2[2017]
ser_obj3 = sorted_obj['二本分数线','文科']
ser_obj3[2018] - ser_obj3[2017]
ser_obj4 = sorted_obj['二本分数线','理科']
ser_obj4[2018] - ser_obj4[2017]
sorted_obj.describe()