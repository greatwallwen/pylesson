'''
时间序列数据分析
时间序列基础
创建时间序列数据
'''

import pandas as pd
from datetime import datetime
import numpy as np
pd.to_datetime('20180828')   # 将datetime转换为Timestamp对象


# 传入多个datetime字符串
date_index = pd.to_datetime(['20180820', '20180828', '20180908'])
date_index


date_index[0]   # 取出第一个时间戳


# 创建时间序列类型的Series对象
date_ser = pd.Series([11, 22, 33], index=date_index)
date_ser



# 指定索引为多个datetime的列表
date_list = [datetime(2018, 1, 1), datetime(2018, 1, 15),
             datetime(2018, 2, 20), datetime(2018, 4, 1),
             datetime(2018, 5, 5), datetime(2018, 6, 1)]
time_se = pd.Series(np.arange(6), index=date_list)
time_se


data_demo = [[11, 22, 33], [44, 55, 66],
             [77, 88, 99], [12, 23, 34]]
date_list = [datetime(2018, 1, 23), datetime(2018, 2, 15),
             datetime(2018, 5, 22), datetime(2018, 3, 30)]
time_df = pd.DataFrame(data_demo, index=date_list)
time_df


'''
通过时间戳索引选取子集
'''

# 指定索引为多个日期字符串的列表
date_list = ['2015/05/30', '2017/02/01',
             '2015.6.1', '2016.4.1',
             '2017.6.1', '2018.1.23']
# 将日期字符串转换为DatetimeIndex
date_index = pd.to_datetime(date_list)
# 创建以DatetimeIndex 为索引的Series对象
date_se = pd.Series(np.arange(6), index=date_index)
date_se


# 根据位置索引获取数据
time_se[3]


date_time = datetime(2015, 6, 1)
date_se[date_time]


date_se['20150530']



date_se['2016-04-01']




date_se['2018/01/23']



date_se['6/1/2017']



date_se['2015']  # 获取2015年的数据


# 扔掉2016-1-1之前的数据
sorted_se = date_se.sort_index()
sorted_se.truncate(before='2016-1-1')



# 扔掉2016-7-31之后的数据
sorted_se.truncate(after='2016-7-31')


'''固定频率的时间序列

 创建固定频率的时间序列
'''

# 创建DatetimeIndex对象时，只传入开始日期与结束日期
pd.date_range('2018/08/10', '2018/08/20')


# 创建DatetimeIndex对象时，传入start与periods参数
pd.date_range(start='2018/08/10', periods=5)


# 创建DatetimeIndex对象时，传入end与periods参数
pd.date_range(end='2018/08/10', periods=5)


dates_index = pd.date_range('2018-01-01',         # 起始日期
                            periods=5,            # 周期
                            freq='W-SUN')         # 频率
dates_index



ser_data = [12, 56, 89, 99, 31]
pd.Series(ser_data, dates_index)



# 创建DatetimeIndex，并指定开始日期、产生日期个数、默认的频率，以及时区
pd.date_range(start='2018/8/1 12:13:30', periods=5,
              tz='Asia/Hong_Kong')

#规范化时间戳
pd.date_range(start='2018/8/1 12:13:30', periods=5,
              normalize=True, tz='Asia/Hong_Kong')

'''
时间序列的频率、偏移量
'''
pd.date_range(start='2018/2/1', end='2018/2/28', freq='5D')


from pandas.tseries.offsets import *
DateOffset(months=4, days=5)


Week(2) + Hour(10)


# 生成日期偏移量
date_offset  = Week(2) + Hour(10)
pd.date_range('2018/3/1', '2018/3/31', freq=date_offset)


'''时间序列数据的移动
'''


date_index = pd.date_range('2018/01/01', periods=5)
time_ser = pd.Series(np.arange(5) + 1, index=date_index)
time_ser


# 向后移动一次
time_ser.shift(1)

# 向前移动一次
time_ser.shift(-1)


'''时间周期及计算
 创建时期对象
'''

# 创建Period对象，表示从2018-01-01到2018-12-31之间的时间段
pd.Period(2018)

# 表示从2017-06-01到2017-06-30之间的整月时间
period = pd.Period('2017/6')
period


period + 1   # Period对象加上一个整数


period - 5    # Period对象减去一个整数


# 创建一个与period频率相同的时期
other_period = pd.Period(201201, freq='M' )
period - other_period

period_index = pd.period_range('2012.1.8', '2012.5.31', freq='M')
period_index


str_list = ['2010', '2011', '2012']
pd.PeriodIndex(str_list, freq='A-DEC')

period_ser = pd.Series(np.arange(5), period_index)
period_ser


'''时期的频率转换
'''

# 创建时期对象
period = pd.Period('2017', freq='A-DEC')
period.asfreq('M', how='start')

period.asfreq('M', how='end')


'''重采样
重采样方法（resample）
'''

date_index = pd.date_range('2017.7.8', periods=30)
time_ser = pd.Series(np.arange(30), index=date_index)
time_ser


time_ser.resample('W-MON', how='mean')

time_ser.resample('W-MON').mean()

time_ser.resample('W-MON', closed='left').mean()


'''降采样
'''


date_index = pd.date_range('2018/06/01', periods=30)
shares_data = np.random.rand(30)
time_ser = pd.Series(shares_data, index=date_index)
time_ser

time_ser.resample('7D').ohlc()  # OHLC重采样

# 通过groupby技术实现降采样
time_ser.groupby(lambda x: x.week).mean()


'''升采样
'''


data_demo = np.array([['101', '210', '150'], ['330', '460', '580']])
date_index = pd.date_range('2018/06/10', periods=2, freq='W-SUN')
time_df = pd.DataFrame(data_demo, index=date_index,
columns=['A产品', 'B产品', 'C产品'])
time_df

time_df.resample('D').asfreq()


time_df.resample('D').ffill()


'''数据统计—滑动窗口
'''

year_data = np.random.randn(365)
date_index = pd.date_range('2017-01-01', '2017-12-31', freq='D')
ser = pd.Series(year_data, date_index)
ser.head()

roll_window = ser.rolling(window=10)
roll_window

roll_window.mean()


import matplotlib.pyplot as plt
# get_ipython().run_line_magic('matplotlib', 'inline')
ser.plot(style='y--')
ser_window = ser.rolling(window=10).mean()
ser_window.plot(style='b')


'''案例—股票预测分析
功能实现
'''

# 导入需要使用的包
import pandas as pd
import datetime
import matplotlib.pylab as plt
# 导入统计模型ARIMA与相关函数
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# 解决matplotlib显示中文问题
# 指定默认字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 解决保存图像是负号'-'显示为方块的问题
plt.rcParams['axes.unicode_minus'] = False


# 读取历史股票数据
data_path = open(r'../mydata/五粮液股票数据.csv')
shares_info = pd.read_csv(data_path)
shares_info


# 将“交易日期”一列设置为行索引
dates = pd.to_datetime(shares_info['交易日期'].values,
                       format='%Y%m%d')
shares_info = shares_info.set_index(dates)
shares_info

plt.plot(shares_info['收盘价'])
plt.title('股票每日收盘价')
plt.show()

#  按周重采样
shares_info_week = shares_info['收盘价'].resample('W-MON').mean()
# 训练数据
train_data = shares_info_week['2014': '2017']
plt.plot(train_data)
plt.title('股票周收盘价均值')
plt.show()

# 分析ACF系数
acf = plot_acf(train_data,lags=20)
plt.title('股票指数的ACF')
plt.show()

# 分析PACF
pacf = plot_pacf(train_data,lags=20)
plt.title('股票指数的PACF')
plt.show()

train_diff = train_data.diff()
diff=train_diff.dropna()
plt.figure()
plt.plot(diff)
plt.title('一阶差分')
plt.show()

acf_diff = plot_acf(diff,lags=20)
plt.title('一阶差分的ACF')
plt.show()

pacf_diff = plot_pacf(diff,lags=20)
plt.title('一阶差分的PACF')
plt.show()

# 创建ARIMA模型
model = ARIMA(train_data, order=(1, 1, 1), freq='W-MON')
# 拟合模型
arima_result = model.fit()
# 通过summary()方法输出关于ARIMA模型中的详细参数说明。
arima_result.summary()

pred_vals = arima_result.predict('2018-01-01','2018-02-26',
                                 dynamic=True, typ='levels')
stock_forcast = pd.concat([shares_info_week, pred_vals],
                          axis=1,
                          keys=['original', 'predicted'])
plt.figure()
plt.plot(stock_forcast)
plt.title('真实值vs预测值')
plt.show()

