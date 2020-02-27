'''
案例—
读取2004-2016年的流感数据，并拼接为一个数据框；
读入人口数据，按年份和地区对流感数据填充人口数。
'''
import pandas as pd
import numpy as np
import os
import re
from prettytable import PrettyTable

# 1. 流感数据的读取与清洗
#
# 2. 读取第一年流感数据
# 首先读取第一年的数据，并展示查看数据查看其格式

# os.chdir('Desktop/')                        # 设置工作路径为C盘桌面
dat0 = pd.read_csv('../mydata/proj_1_data/by_year/2004.csv', encoding = "gbk") # 读取数据，命名为dat0
dat0.head()# 展示数据前5行
dat0.tail() # 展示数据后5行
# 从这里我们可以看出数据框的列名与实际需要的列名不符，并且数据框头尾均有不需要的空行。
#
# 3. 对第一年的数据进行预处理
# 针对上一步中所看出的现象对第1年的数据进行预处理，主要的步骤是重塑列名以及删除多余的列。
dat0.drop("Unnamed: 0", axis =1, inplace= True)        # 删除第一列
col_name = dat0.iloc[1]                                # 选取真实列名所在的第1行
dat0.columns = col_name                                # 更改列名
dat0.drop([0, 1, len(dat0)-1], axis =0, inplace= True) # 删除多余的行
dat0.head()
# 查看展示出的数据，可以发现据的index被删除行的时候弄乱了，
# 于是在这一部分我们对index进行重置，并对数据新增加年份变量。
dat0.reset_index(inplace = True, drop=True) # 重新设置被打乱的index
dat0["年份"] = 2004                         # 添加年份变量
dat0.head()                                 # 展示数据

# 4. 批量读取连接数据
# 针对对第一年数据的预处理，我们可以知道对后续的数据的预处理操作，
# 于是在这里自定义函数用于对后几年的数据进行预处理和重塑变量。

# 自定义函数Preprogress对后几年数据需要进行的预处理
# 传入参数为df：数据框；year：年份数
# 返回处理过的数据框
def Preprogress(df, year):
    df.drop("Unnamed: 0", axis =1, inplace= True)       # 删除第0列
    df.drop([0, 1 , len(df)-1], axis =0, inplace= True) # 删除头两行和后一行
    df["年份"] = year                                   # 重塑年份变量
    return(df)                                          # 返回值

# 在进行批量读取数据之前我们先获取需要读取的文件名，
# 通过os.listdir得到数据的文件名列表，并删除之前已经读取过的2004年的数据。

file_name = os.listdir('mydata/by_year') # 获得by_year文件夹内的文件名[list形式]
file_name.remove("2004.csv")      # 剔除已经读入的2004年的数据
file_name                         # 查看列表

# 定义函数用于批量读取及拼接数据，并在读取过程中使用上述Preprogress的函数进行预处理。

#5. 自义函数ReadYear用于批量读取拼接数据
## 传入参数file_name:文件名列表;the_path:路径
## 返回值other_data：拼接过的数据
def ReadYear(file_name, the_path):
    list = []                                                        # 建立空列表用于存放数据
    for i in range(len(file_name)):                                  # 通过循环遍历读取文件
        df = pd.read_csv(the_path + file_name[i] , encoding = "gbk") # 读取数据
        year = 2004+i+1                                              # 依次累加年份
        Preprogress(df, year)                                        # 进行预处理及其重塑变量
        list.append(df)                                              # 将处理过后的数据框添加到list中
        other_data = pd.concat(list)                                 # 使用concat合并list内的数据
    return(other_data)                                               # 返回值

other_data = ReadYear(file_name, "mydata/by_year/")                         # 批量读取数据
other_data.head()

# 拼接后的数据如上所示，而这份数据还需要与之前读取的2004年的数据所连接，
# 一般情况下需要通过列名进行拼接，
# 因此我们需要重塑other_data的列名，使其dat一致。

other_data.columns = col_name.append(pd.Series("年份")) # 重塑数据的列名
other_data.head()                                       # 展示数据的前5行

# 接下来就可以直接通过concat那两份数据连接起来，
# 这里需要注意的是连接的数据需要放在一个list内。
# 而且我们可以发现数据中存在部分的缺失值，在这里我们使用0对缺失值进行填补。

flu_data = pd.concat([dat0, other_data]) # 连接数据，命名为flu_data
flu_data.fillna(0, inplace = True)       # 使用0填充缺失值
flu_data.head()                          # 展示数据前5行

# 6. 检查数据
# 到这一步的时候，我们的第一个流感数据就算是大概出来了，
# 但是该数据也不太规整，
# 所以我们先对地区这一列进行一个计数，用于检查。

flu_data["地区"].value_counts() # 对数据进行计数

# 通过输出现象可以看出数据缺失存在一些问题，
# 如部分数据中存在空格；黑龙江有“黑龙江”和“黑龙江省”两种表现形式；
# 在人口数据中没有建设兵团这一类型，需要删除这一类型所在的行。
# 针对这些问题我们还需要进行预处理。

flu_data["地区"] = flu_data["地区"].apply(lambda x: x.replace(" ", "")) # 替换文字中的空格
flu_data = flu_data.loc[flu_data["地区"] != "建设兵团"]                 # 删除地区为建设
flu_data.loc[flu_data['地区'] =='黑龙江','地区']='黑龙江省'             # 将黑龙江替换为黑龙江省

flu_data["地区"].value_counts()                                         # 再次检查地区列

# 可见进行处理的地区变量的每一项均为13个，对应读入的13年的数据，
# 说明数据处理规范。之后开始对人口数据进入读取和处理。


# 7. 人口数据的清洗与重塑
# 读取人口数据，并展示查看它的前后5行。

people = pd.read_csv("mydata/people.csv",error_bad_lines=False ) # 读取人口数据，命名为people
people.head()                                       # 展示数据的前5行
people.tail() # 展示数据的后5行

# 通过观察数据，我们可以发现数据的列名位于第2行，
# 前3行和后两行均是需要剔除的多余数据，通过先前使用过的方法对数据进行处理。

people.columns = people.iloc[2]                                            # 用第2行作为列名
people.drop([0,1,2,len(people)-1,len(people)-2], axis = 0, inplace = True) # 删除多余的行
people.reset_index(inplace=True, drop=True)                                # 删除多余的行
people.head()                                                              # 展示数据的前5行

# 通过观察数据，我们可以发现人口数据的部分地区名与流感数据的地区名不一致，
# 比如对于内蒙古，流感数据中的表现形式为“内蒙古”，
# 而人口数据中的表现形式为“内蒙古自治区”。
# 而后续对流感数据填充人口数时需要同时通过地区和年份两值进行填充，
# 因此需要对统一二者地区名的格式，
# 在这里选择统一对人口数据去掉“自治区”三个字进行处理。

## 统一地区名的格式
people.loc[people['地区'] == '内蒙古自治区','地区']='内蒙古'
people.loc[people['地区'] == '广西壮族自治区','地区']='广西'
people.loc[people['地区'] == '西藏自治区','地区']='西藏'
people.loc[people['地区'] == '宁夏回族自治区','地区']='宁夏'
people.loc[people['地区'] == '新疆维吾尔自治区','地区']='新疆'
# 规范了地区名之后，为了方便数据的填充，
# 我们需要对人口数据数据进行重塑，
# 以地区、年份、总人口数三个变量的形式进行表示，
# 使宽数据变为长数据。下列展示了数据重塑及其预处理的过程。

peo_name = list(people.columns)                          # 获取people的变量名
peo_name.remove("地区")                                  # 去除地区变量，得到年份数据
change_people = pd.melt(people, id_vars=["地区"], value_vars=peo_name, \
                        var_name="年份", value_name="总人口数")                        # 通过melt重塑数据
change_people["年份"] = change_people["年份"].apply(lambda x: re.findall("\d+", x)[0]) # 去除年份的“年”字
change_people["年份"] = change_people["年份"].astype(np.int)                           # 将年份转换为数值形式
change_people.head()

# 8. 拼接数据
# 结束了对流感数据及人口数据的读取和处理，
# 接下来我们需要对两个数据进行拼接，
# 使用merge函数，按年份和地区对值进填充。

result = pd.merge(flu_data, change_people, on=['年份', '地区'])
result.dtypes
# 对数值变量的变量类型进行转换

change_list = ['发病率','死亡率','总人口数','发病数','死亡数']
result[change_list] = result[change_list].apply(pd.to_numeric)
result.head()
from tabulate import tabulate
import wcwidth
tabulate.WIDE_CHARS_MODE = True
headers=result.columns.to_list()
headers.insert(0,'索引')
print(tabulate(result.head(),headers=headers, tablefmt='psql'))

# 通过以上的操作，成功进行了对数据的处理已经拼接。


