import numpy as np

'''
认识NumPy数组对象
'''
# >>>data = np.arange(12).reshape(3, 4)  # 创建一个3行4列的数组
# >>>data
# >>>type(data))
# >>>data.ndim         # 数组维度的个数，输出结果2，表示二维数组
# 2
# In [6]:
# >>>data.shape        # 数组的维度，输出结果（3，4），表示3行4列
# (3, 4)
# In [7]:
# >>>data.size         # 数组元素的个数，输出结果12，表示总共有12个元素
# 12
# In [8]:
# data.dtype # 数组元素的类型，输出结果dtype('int64'),表示元素类型都是int64

'''
创建numpy数组
'''
data1 = np.array([1, 2, 3])                   # 创建一个一维数组

data2 = np.array([[1, 2, 3], [4, 5, 6]])   # 创建一个二维数组


np.zeros((3, 4))
#
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])

np.ones((3, 4))

# array([[1., 1., 1., 1.],
#        [1., 1., 1., 1.],
#        [1., 1., 1., 1.]])

np.empty((5, 2))#里面的数据都是随机的

# array([[3.62646160e-316, 2.37151510e-322],
#        [0.00000000e+000, 0.00000000e+000],
#        [0.00000000e+000, 1.16095484e-028],
#        [7.52736939e+252, 3.01478103e-110],
#        [6.48224638e+170, 3.67145870e+228]])

np.arange(1, 20, 5)

np.array([1, 2, 3, 4], float)

np.ones((2, 3), dtype='float64')

# Note:有些数组元素的后面会跟着一个小数点，
# 而有些元素后面没有，比如1和1.，产生这种现象，
# 主要是因为元素的数据类型不同所导致的。

'''
转换数据类型
'''

data = np.array([[1, 2, 3], [4, 5, 6]])

data.dtype

# dtype('int32')

float_data = data.astype(np.float64) # 数据类型转换为float64

# float_data.dtype

float_data = np.array([1.2, 2.3, 3.5])

# float_data

# array([1.2, 2.3, 3.5])

int_data = float_data.astype(np.int64) # 数据类型转换为int64

# array([1, 2, 3], dtype=int64)

str_data = np.array(['1', '2', '3'])

int_data = str_data.astype(np.int64)

int_data
# Out[32]:
# array([1, 2, 3], dtype=int64)

'''
数组运算
矢量化运算
'''

data1 = np.array([[1, 2, 3], [4, 5, 6]])

data2 = np.array([[1, 2, 3], [4, 5, 6]])

data1 + data2        # 数组相加

# array([[ 2,  4,  6],
#        [ 8, 10, 12]])

data1 * data2        # 数组相乘
# Out[37]:
# array([[ 1,  4,  9],
#        [16, 25, 36]])

data1 - data2        # 数组相减
# Out[38]:
# array([[0, 0, 0],
#        [0, 0, 0]])

data1 / data2       # 数组相除

'''
数组广播
In [40]:
import numpy as np
'''

arr1 = np.array([[0], [1], [2], [3]])

arr1.shape
# Out[42]:
# (4, 1)
# In [43]:
arr2 = np.array([1, 2, 3])

arr2.shape
# Out[44]:
# (3,)

arr1 + arr2

'''
数组与标量间的运算

'''


data1 = np.array([[1, 2, 3], [4, 5, 6]])

data2 = 10

data1 + data2      # 数组相加
# Out[49]:
# array([[11, 12, 13],
#        [14, 15, 16]])

data1 * data2       # 数组相乘

# array([[10, 20, 30],
#        [40, 50, 60]])

data1 - data2        # 数组相减
# Out[51]:
# array([[-9, -8, -7],
#        [-6, -5, -4]])

data1 / data2       # 数组相除
# Out[52]:
# array([[0.1, 0.2, 0.3],
#        [0.4, 0.5, 0.6]])
'''
ndarray的索引和切片
整数索引和切片的基本使用
'''

arr = np.arange(8)    # 创建一个一维数组

arr
# Out[55]:
# array([0, 1, 2, 3, 4, 5, 6, 7])

arr[5]                  # 获取索引为5的元素
# Out[56]:
5

arr[3:5]                # 获取索引为3~5的元素，但不包括5
# Out[57]:
# array([3, 4])

arr[1:6:2]              # 获取索引为1~6的元素，步长为2
# Out[58]:
# array([1, 3, 5])

arr2d = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) # 创建二维数组

arr2d
# Out[61]:
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])

arr2d[1]            # 获取索引为1的元素
# Out[62]:
# array([4, 5, 6])

arr2d[0, 1]        # 获取位于第0行第1列的元素
# Out[63]:
# 2

arr2d[:2]
# Out[64]:
# array([[1, 2, 3],
#        [4, 5, 6]])

arr2d[0:2, 0:2]
# Out[65]:
# array([[1, 2],
#        [4, 5]])

arr2d[1, :2]
'''
花式（数组）索引的基本使用
'''

demo_arr = np.empty((4, 4))               # 创建一个空数组
for i in range(4):
    demo_arr[i] = np.arange(i, i + 4)   # 动态地为数组添加元素

demo_arr
# Out[69]:
# array([[0., 1., 2., 3.],
#        [1., 2., 3., 4.],
#        [2., 3., 4., 5.],
#        [3., 4., 5., 6.]])

demo_arr[[0, 2]]        # 获取索引为[0,2]的元素
# Out[70]:
# array([[0., 1., 2., 3.],
#        [2., 3., 4., 5.]])

demo_arr[[1, 3], [1, 2]]     # 获取索引为(1,1)和(3,2)的元素
# Out[71]:
# array([2., 5.])
'''
布尔型

'''
# 存储学生姓名的数组
student_name = np.array(['Tom', 'Lily', 'Jack', 'Rose'])

student_name

# array(['Tom', 'Lily', 'Jack', 'Rose'], dtype='<U4')

# 存储学生成绩的数组
student_score = np.array([[79, 88, 80], [89, 90, 92], [83, 78, 85], [78, 76, 80]])

student_score
# Out[75]:
# array([[79, 88, 80],
#        [89, 90, 92],
#        [83, 78, 85],
#        [78, 76, 80]])

# 对student_name和字符串“Jack”通过运算符产生一个布尔型数组
student_name == 'Jack'
# Out[76]:
# array([False, False,  True, False])

# 将布尔数组作为索引应用于存储成绩的数组student_score，
# 返回的数据是True值对应的行
student_score[student_name=='Jack']
# Out[77]:
# array([[83, 78, 85]])

student_score[student_name=='Jack', :1]

'''
数组的转置和轴对称
'''

arr = np.arange(12).reshape(3, 4)

arr
# Out[80]:
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

arr.T      # 使用T属性对数组进行转置
# Out[81]:
# array([[ 0,  4,  8],
#        [ 1,  5,  9],
#        [ 2,  6, 10],
#        [ 3,  7, 11]])

arr = np.arange(16).reshape((2, 2, 4))

arr
# Out[83]:
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7]],
#
#        [[ 8,  9, 10, 11],
#         [12, 13, 14, 15]]])

arr.transpose(1, 2, 0)   # 使用transpose()方法对数组进行转置
# Out[84]:
# array([[[ 0,  8],
#         [ 1,  9],
#         [ 2, 10],
#         [ 3, 11]],
#
#        [[ 4, 12],
#         [ 5, 13],
#         [ 6, 14],
#         [ 7, 15]]])

arr
# Out[85]:
# array([[[ 0,  1,  2,  3],
#         [ 4,  5,  6,  7]],
#
#        [[ 8,  9, 10, 11],
#         [12, 13, 14, 15]]])

arr.swapaxes(1, 0)    # 使用swapaxes方法对数组进行转置
'''
NumPy通用函数
'''

arr = np.array([4, 9, 16])

np.sqrt(arr)

np.abs(arr)
# Out[89]:
# array([ 4,  9, 16])

np.square(arr)
# Out[90]:
# array([ 16,  81, 256], dtype=int32)

x = np.array([12, 9, 13, 15])

y = np.array([11, 10, 4, 8])

np.add(x, y)      # 计算两个数组的和
# Out[93]:
# array([23, 19, 17, 23])

np.multiply(x, y) # 计算两个数组的乘积
# Out[94]:
# array([132,  90,  52, 120])

np.maximum(x, y)  # 两个数组元素级最大值的比较
# Out[95]:
# array([12, 10, 13, 15])

np.greater(x, y)  # 执行元素级的比较操作
'''
利用NumPy数组进行数据处理
将条件逻辑转为数组运算
'''

arr_x = np.array([1, 5, 7])

arr_y = np.array([2, 6, 8])

arr_con = np.array([True, False, True])

result = np.where(arr_con, arr_x, arr_y)

result
'''
2.8.2 数组统计运算
'''

arr = np.arange(10)

arr.sum()      # 求和
# Out[103]:
# 45

arr.mean()     # 求平均值
# Out[104]:
# 4.5

arr.min()      # 求最小值
# Out[105]:
# 0

arr.max()       # 求最大值
# Out[106]:
# 9

arr.argmin()   # 求最小值的索引
# Out[107]:
# 0

arr.argmax()   # 求最大值的索引
# Out[108]:
# 9

arr.cumsum()   # 计算元素的累计和
# Out[109]:
# array([ 0,  1,  3,  6, 10, 15, 21, 28, 36, 45], dtype=int32)

arr.cumprod()  # 计算元素的累计积
'''
数组排序
'''

arr = np.array([[6, 2, 7], [3, 6, 2], [4, 3, 2]])

arr


arr.sort()

arr
# Out[114]:
# array([[2, 6, 7],
#        [2, 3, 6],
#        [2, 3, 4]])

arr = np.array([[6, 2, 7], [3, 6, 2], [4, 3, 2]])

arr
# Out[116]:
# array([[6, 2, 7],
#        [3, 6, 2],
#        [4, 3, 2]])

arr.sort(0)       # 沿着编号为0的轴对元素排序

arr
# Out[118]:
# array([[3, 2, 2],
#        [4, 3, 2],
#        [6, 6, 7]])
'''
检索数组元素
'''

arr = np.array([[1, -2, -7], [-3, 6, 2], [-4, 3, 2]])

arr
# Out[120]:
# array([[ 1, -2, -7],
#        [-3,  6,  2],
#        [-4,  3,  2]])

np.any(arr > 0)      # arr的所有元素是否有一个大于0
# Out[121]:
# True

np.all(arr > 0)      # arr的所有元素是否都大于0
'''
唯一化及其他集合逻辑
'''

arr = np.array([12, 11, 34, 23, 12, 8, 11])

np.unique(arr)
# Out[124]:
# array([ 8, 11, 12, 23, 34])

np.in1d(arr, [11, 12])
'''
线性代数模块
'''

arr_x = np.array([[1, 2, 3], [4, 5, 6]])

arr_y = np.array([[1, 2], [3, 4], [5, 6]])

arr_x.dot(arr_y)   # 等价于np.dot(arr_x, arr_y)
# Out[128]:
# array([[22, 28],
#        [49, 64]])
'''
随机数模块
'''


np.random.rand(3, 3)     # 随机生成一个二维数组
# Out[130]:
# array([[0.08291435, 0.12472886, 0.63138229],
#        [0.90699123, 0.47094038, 0.89587174],
#        [0.34258862, 0.37672691, 0.47287096]])

np.random.rand(2, 3, 3) # 随机生成一个三维数组
# Out[131]:
# array([[[0.27381047, 0.08982023, 0.91901954],
#         [0.27041891, 0.02776499, 0.28179073],
#         [0.71968803, 0.00389243, 0.57802953]],
#
#        [[0.04909628, 0.15225786, 0.44995308],
#         [0.07292318, 0.00955777, 0.77968477],
#         [0.94597236, 0.93449858, 0.70178838]]])

np.random.seed(0)   # 生成随机数的种子

np.random.rand(5)   # 随机生成包含5个元素的浮点数组
# Out[134]:
# array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

np.random.seed(0)

np.random.rand(5)
# Out[136]:
# array([0.5488135 , 0.71518937, 0.60276338, 0.54488318, 0.4236548 ])

np.random.seed()

np.random.rand(5)

# array([0.14604275, 0.24502934, 0.58934455, 0.73427067, 0.2362898 ])

'''
案例—酒鬼漫步
'''
# 导入numpy包
# import numpy as np
steps = 20
draws = np.random.randint(0, 2, size=steps)
# 当元素为1时，direction_steps为1，
# 当元素为0时，direction_steps为-1
direction_steps = np.where(draws > 0, 1, -1)
# 使用cumsum()计算步数累计和
distance = direction_steps.cumsum()

# 使用max()计算向前走的最远距离
distance.max()
# 使用min()计算向后走的最远距离
distance.min()
# 15米换算成步数
steps = 30 #15 / 0.5
(np.abs(distance) >= steps).argmax()
