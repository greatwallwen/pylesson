#!/usr/bin/env python
# coding: utf-8

'''Matplotlib—绘制图表
通过figure()函数创建画布
'''

import matplotlib.pyplot as plt
# from IPython import get_ipython

# get_ipython().run_line_magic('matplotlib', 'inline')


import numpy as np
data_one = np.arange(100, 201)  # 生成包含100~200的数组
plt.plot(data_one)                # 绘制data1折线图
plt.show()


# 创建新的空白画布，返回Figure实例
figure_obj = plt.figure()


# In[4]:


data_two = np.arange(200, 301)      # 生成包含200~300的数组
plt.figure(facecolor='gray')    # 创建背景为灰色的新画布
plt.plot(data_two)                    # 通过data2绘制折线图
plt.show()


'''
通过subplot()函数创建单个子图
'''
nums = np.arange(0, 101)    # 生成0~100的数组
# 分成2*2的矩阵区域，占用编号为1的区域，即第1行第1列的子图
plt.subplot(221)
# 在选中的子图上作图
plt.plot(nums, nums)
# 分成2*2的矩阵区域，占用编号为2的区域，即第1行第2列的子图
plt.subplot(222)
# 在选中的子图上作图
plt.plot(nums, -nums)
# 分成2*1的矩阵区域，占用编号为2的区域，即第2行的子图
plt.subplot(212)
# 在选中的子图上作图
plt.plot(nums, nums**2)
# 在本机上显示图形
plt.show()


'''通过subplots()函数创建多个子图
'''

# 生成包含1～100之间所有整数的数组
nums = np.arange(1, 101)
# 分成2*2的矩阵区域，返回子图数组axes
fig, axes = plt.subplots(2, 2)
ax1 = axes[0, 0]  # 根据索引［0，0］从Axes对象数组中获取第1个子图
ax2 = axes[0, 1]   # 根据索引［0，1］从Axes对象数组中获取第2个子图
ax3 = axes[1, 0]   # 根据索引［1，0］从Axes对象数组中获取第3个子图
ax4 = axes[1, 1]   # 根据索引［1，1］从Axes对象数组中获取第4个子图
# 在选中的子图上作图
ax1.plot(nums, nums)
ax2.plot(nums, -nums)
ax3.plot(nums, nums**2)
ax4.plot(nums, np.log(nums))
plt.show()


'''
通过add_subplot()方法添加和选中子图
'''
# 引入matplotlib包
import matplotlib.pyplot as plt
import numpy as np
# 创建Figure实例
fig = plt.figure()
# 添加子图
fig.add_subplot(2, 2, 1)
fig.add_subplot(2, 2, 2)
fig.add_subplot(2, 2, 4)
fig.add_subplot(2, 2, 3)
# 在子图上作图
random_arr = np.random.randn(100)
# 默认是在最后一次使用subplot的位置上作图，即编号为3的位置
plt.plot(random_arr)
plt.show()


'''
添加各类标签
'''

data = np.arange(0, 1.1, 0.01)
plt.title("Title")      # 添加标题
plt.xlabel("x")         # 添加x轴的名称
plt.ylabel("y")         # 添加y轴的名称
# 设置x和y轴的刻度
plt.xticks([0, 0.5, 1])
plt.yticks([0, 0.5, 1.0])
plt.plot(data, data**2)         # 绘制y=x^2曲线
plt.plot(data, data**3)         # 绘制y=x^3曲线
plt.legend(["y=x^2", "y=x^3"])   # 添加图例
plt.show()              # 在本机上显示图形


'''
绘制常见类型图表
'''

arr_random = np.random.randn(100)   # 创建随机数组
plt.hist(arr_random, bins=8, color='g', alpha=0.7) # 绘制直方图
plt.show()  # 显示图形



# 创建包含整数0~50的数组，用于表示x轴的数据
x = np.arange(51)
# 创建另一数组，用于表示y轴的数据
y = np.random.rand(51) * 10
plt.scatter(x, y)   # 绘制散点图
plt.show()

# 创建包含0~4的一维数组
x = np.arange(5)
# 从上下限范围内随机选取整数，创建两个2行5列的数组
y1, y2 = np.random.randint(1, 31, size=(2, 5))
width = 0.25                                # 条形的宽度
ax = plt.subplot(1, 1, 1)                # 创建一个子图
ax.bar(x, y1, width, color='r')         # 绘制红色的柱形图
ax.bar(x+width, y2, width, color='g')  # 绘制另一个绿色的柱形图
ax.set_xticks(x+width)                    # 设置x轴的刻度
# 设置x轴的刻度标签
ax.set_xticklabels(['January', 'February', 'March', 'April ', 'May '])
plt.show()                                  # 显示图形



data = np.arange(1, 3, 0.3)
# 绘制直线，颜色为青色，标记为“x”，线型为长虚线
plt.plot(data, color="c", marker="x", linestyle="--")
# 绘制直线，颜色为品红，标记为实心圆圈，线型为短虚线
plt.plot(data+1, color="m", marker="o", linestyle=":")
# 绘制直线，颜色为黑色，标记为五边形，线型为短点相间线
plt.plot(data+2, color="k", marker="p", linestyle="-.")
# 也可采用下面的方式绘制三条不同颜色、标记和线型的直线
# plt.plot(data, 'cx--', data+1, 'mo:', data+2, 'kp-.')
plt.show()

'''
 本地保存图形
'''


# 创建包含100个数值的随机数组

random_arr = np.random.randn(100)
# 将随机数组的数据绘制线形图
plt.plot(random_arr)
plt.show()


'''
seaborn—绘制统计图形

'''
import seaborn as sns
# get_ipython().run_line_magic('matplotlib', 'inline')
# import numpy as np
sns.set()                      # 显式调用set()获取默认绘图
np.random.seed(0)            # 确定随机数生成器的种子
arr = np.random.randn(100)        # 生成随机数组
ax = sns.distplot(arr, bins=10)  # 绘制直方图

# 创建包含500个位于[0，100]之间整数的随机数组
array_random = np.random.randint(0, 100, 500)
# 绘制核密度估计曲线
sns.distplot(array_random, hist=False, rug=True)
plt.show()#pycharm中需要加上

# 创建DataFrame对象
import pandas as pd
dataframe_obj = pd.DataFrame({"x": np.random.randn(500),"y": np.random.randn(500)})
# 绘制散布图
sns.jointplot(x="x", y="y", data=dataframe_obj)
plt.show()#pycharm中需要加上

# 绘制二维直方图
sns.jointplot(x="x", y="y", data=dataframe_obj, kind="hex")
plt.show()#pycharm中需要加上

# 核密度估计
sns.jointplot(x="x", y="y", data=dataframe_obj, kind="kde")
plt.show()#pycharm中需要加上

# 加载seaborn中的数据集
dataset = sns.load_dataset("tips")
# 绘制多个成对的双变量分布
sns.pairplot(dataset)
plt.show()#pycharm中需要加上

'''
用分类数据绘图
'''


# tips = sns.load_dataset("tips")#有可能网络错误
tips=pd.read_csv("../mydata/seaborn_data/tips.csv")
sns.stripplot(x="day", y="total_bill", data=tips)



# tips = sns.load_dataset("tips")
sns.stripplot(x="day", y="total_bill", data=tips, jitter=True)

sns.swarmplot(x="day", y="total_bill", data=tips)

sns.boxplot(x="day", y="total_bill", data=tips)

sns.violinplot(x="day", y="total_bill", data=tips)

sns.barplot(x="day", y="total_bill", data=tips)

sns.pointplot(x="day", y="total_bill", data=tips)
plt.show()#pycharm中需要加上

'''
bokeh—交互式可视化库
通过Plotting绘制图形
目前只能通过浏览器来运行
'''

from bokeh.plotting import figure, output_notebook, show
# 输出到电脑屏幕上
output_notebook()
fig_obj = figure(plot_width=400, plot_height=400)
# 添加矩形框，标有大小、颜色和alpha值
fig_obj.square([2, 5, 6, 4], [2, 3, 2, 1], size=20, color="navy")
# 在默认的浏览器中显示图表
show(fig_obj)


'''
案例—画图分析某年旅游景点数据
功能实现
'''


import pandas as pd
import numpy as np
# 使用read_csv()方法进行读取
scenery_file_path = open(r'../mydata/风景名胜区.csv')
scenery_data = pd.read_csv(scenery_file_path)
scenery_data


# 计算‘总面积(平方公里)’的平均数，并保留一位小数
area = float("{:.1f}".format(
scenery_data['总面积(平方公里)'].mean()))
# 计算‘游客量(万人次)’平均数，并保留一位小数
tourist = float("{:.1}".format(
scenery_data['游客量(万人次)'].mean()))
# 将上述计算的平均值，使用fillna()函数，字典映射的形式进行填充
values = {"总面积(平方公里)":area,"游客量(万人次)":tourist}
scenery_data = scenery_data.fillna(value=values)
scenery_data.head



# 通过groupby()函数按“省份”一列拆分scenery_data
data = scenery_data.groupby("省份")
# 显示“河北”分组的数据
hebei_scenery = dict([x for x in data])['河北']
hebei_scenery


import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['font.sans-serif']=['SimHei']  # 正常显示中文标签
plt.rcParams['axes.unicode_minus']=False    # 正常显示负号
area = hebei_scenery['总面积(平方公里)'].values
tourist = hebei_scenery['游客量(万人次)'].values
# 设置尺寸
plt.figure(figsize=(12, 6))
x_num = range(0, len(area))
x_dis = [i + 0.3 for i in x_num]
plt.bar(x_num, area, color='g', width=.3, label='总面积')
plt.bar(x_dis, tourist, color='r', width=.3, label='游客量')
plt.ylabel('单位：平方公里/万人次')
plt.title('河北景点面积及游客数量')
# 设置图例
plt.legend(loc='upper right')
plt.xticks(range(0, 10),['苍岩山', '嶂石岩', '西柏坡-天桂山',
'秦皇岛北戴河','响堂山','娲皇宫','太行大峡谷',
'崆山白云洞','野三坡','承德避暑山庄外八庙'])
plt.show()


import matplotlib.pyplot as plt
every_scenery = hebei_scenery['游客量(万人次)'].values
all_scenery = hebei_scenery['游客量(万人次)'].sum()
# 计算每个景点游客所占百分比  保留两位小数
percentage = (every_scenery/all_scenery)*100
np.set_printoptions(precision=2)
labels  = ['苍岩山', '嶂石岩', '西柏坡-天桂山',
            '秦皇岛北戴河','响堂山','娲皇宫','太行大峡谷',
            '崆山白云洞','野三坡','承德避暑山庄外八庙']
plt.axes(aspect=1)
plt.pie(x= percentage, labels=labels, autopct='%3.2f %%',shadow=True, labeldistance=1.2, startangle = 90,pctdistance = 0.7)
plt.legend(loc='upper left')
plt.show()

