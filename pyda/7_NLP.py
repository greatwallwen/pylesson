#!/usr/bin/env python
# coding: utf-8

'''文本数据分析
文本数据分析工具
'''


import nltk
# nltk.download()    # 打开NLTK下载器


from nltk.corpus import brown       # 导入brown语料库
brown.words()                        # 查看brown库中所有的单词

brown.categories()


'brown中一共有{}个句子'.format(len(brown.sents()))

'brown中一共有{}个单词'.format(len(brown.words()))

''''
文本预处理
分词（包含中英文）
'''

# 原始英文文本
sentence = 'Python is a structured and powerful object-oriented programming language.'
# 将句子切分为单词
words = nltk.word_tokenize(sentence)
words


import jieba
# 原始中文文本
sentence = '南京高等职业技术学院推出网络教学模式，突破传统广受好评'
# 全模式划分中文句子
terms_list = jieba.cut(sentence, cut_all=True)
print('【全模式】：'+ '/'.join(terms_list))
# 精确模式划分中文句子
terms_list = jieba.cut(sentence, cut_all=False)
print('【精确模式】：'+ '/'.join(terms_list))


'''
词性标注
'''


words = nltk.word_tokenize('Python is a structured and powerful object-oriented programming language.')
# 为列表中的每个单词标注词性
nltk.pos_tag(words)


'''词形归一化
'''


# 导入nltk.stem模块的波特词干提取器
from nltk.stem.porter import PorterStemmer
# 按照波特算法提取词干
porter_stem = PorterStemmer()
porter_stem.stem('watched')

porter_stem.stem('watching')


from nltk.stem.lancaster import LancasterStemmer
lancaster_stem = LancasterStemmer()
# 按照兰卡斯特算法提取词干
lancaster_stem.stem('jumped')


lancaster_stem.stem('jumping')


from nltk.stem import SnowballStemmer
snowball_stem = SnowballStemmer('english')
snowball_stem.stem('listened')


snowball_stem.stem('listening')

from nltk.stem import WordNetLemmatizer
# 创建WordNetLemmatizer对象
wordnet_lem = WordNetLemmatizer()
# 还原books单词的基本形式
wordnet_lem.lemmatize('books')

wordnet_lem.lemmatize('went')

wordnet_lem.lemmatize('did')


# 指定went的词性为动词
wordnet_lem.lemmatize('went', pos='v')

wordnet_lem.lemmatize('did', pos='v')


'''删除停用词
'''

from nltk.corpus import stopwords
# 原始文本
sentence = 'Python is a structured and powerful object-oriented programming language.'
# 将英文语句按空格划分为多个单词
words = nltk.word_tokenize(sentence)
words


# 获取英文停用词列表
stop_words = stopwords.words('english')
# 定义一个空列表
remain_words = []
# 如果发现单词不包含在停用词列表中，就保存在remain_words中
for word in words:
    if word not in stop_words:
        remain_words.append(word)
remain_words


'''
文本情感分析
'''
# 用作训练的文本
text_one = 'This is a wonderful book'
text_two = 'I like reading this book very much.'
text_thr = 'This book reads well.'
text_fou = 'This book is not good.'
text_fiv = 'This is a very bad book.'

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.classify import NaiveBayesClassifier
def pret_text(text):
    # 对文本进行分词
    words = nltk.word_tokenize(text)
    # 词形还原
    wordnet_lematizer = WordNetLemmatizer()
    words = [wordnet_lematizer.lemmatize(word) for word in words]
    # 删除停用词
    remain_words = [word for word in words if word not
                    in stopwords.words('english')]
    # True 表示该词在文本中
    return {word: True for word in remain_words}

# 构建训练文本，设定情感分值
train_data = [[pret_text(text_one), 1],
              [pret_text(text_two), 1],
              [pret_text(text_thr), 1],
              [pret_text(text_fou), -1],
              [pret_text(text_fiv), -1]]
# 训练模型
demo_model = NaiveBayesClassifier.train(train_data)


# 测试模型
test_text1 = 'I like this movie very much'
demo_model.classify(pret_text(test_text1))


test_text2 = 'The film is very bad'
demo_model.classify(pret_text(test_text2))

test_text3 = 'The film is terrible'
demo_model.classify(pret_text(test_text3))


'''
文本相似度
'''

import nltk
nltk.data.path.append(r"../mydata/nltk_data")
from nltk import FreqDist

text1 = 'John likes to watch movies'
text2 = 'John also likes to watch football games'
all_text = text1 +" " + text2
# 分词
words = nltk.word_tokenize(all_text)
# 创建FreqDist对象，记录每个单词出现的频率
freq_dist = FreqDist(words)
freq_dist


freq_dist['John']


# 取出n个常用的单词
n = 5
# 返回常用单词列表
most_common_words = freq_dist.most_common(n)
most_common_words



def find_position(common_words):
    """
    查找常用单词的位置
    """
    result = {}
    pos = 0
    for word in common_words:
        result[word[0]] = pos
        pos += 1
    return result
# 记录常用单词的位置
pos_dict = find_position(most_common_words)
pos_dict



def text_to_vector(words):
    '''
       将文本转换为词频向量
    '''
    # 初始化向量
    freq_vec = [0] * n
    # 在“常用单词列表”上计算词频
    for word in words:
       if word in list(pos_dict.keys()):
           freq_vec[pos_dict[word]] += 1
    return freq_vec


# 词频向量
vector1 = text_to_vector(nltk.word_tokenize(text1))
vector1


vector2 = text_to_vector(nltk.word_tokenize(text2))
vector2


from nltk.cluster.util import cosine_distance
cosine_distance(vector1, vector2)


'''文本分类
'''

import random
# 收集数据，用一部分数据来训练，用一部分数据用来测试
names = [(name,'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')]
# 将names的所有元素随机排序
random.shuffle(names)
names



# 特征提取器
def gender_features(word):
    # 特征就是最后一个字母和倒数第二个字母
    return {'最后一个字母':word[-1],'倒数第二个字母':word[-2]}
features = [(gender_features(n),g) for (n,g) in names]
features


train, test = features[500:],features[:500]
# 使用训练集训练模型
classifier = nltk.NaiveBayesClassifier.train(train)


# 通过测试集来估计分类器的准确性
nltk.classify.accuracy(classifier, test)


# 如果一个人的名字是‘Ella，那么这个人是男还是女
classifier.classify({'last_letter': 'Ella'})


# 检查分类器，找出最能够区分名字性别的特征值
classifier.show_most_informative_features(5)


'''
案例—商品评价信息分析
'''

import pandas as pdaveraged
from nltk import FreqDist
import jieba
file_path = open(r'../mydata/商品评价信息.csv')
file_data = pd.read_csv(file_path)
file_data


# 删除重复的评价
file_data = file_data.drop_duplicates()
file_data


# 使用精确模式划分中文句子
cut_words = jieba.lcut(str(file_data['评价信息'].values), cut_all = False)
cut_words


# 加载停用词表
file_path = open(r'../mydata/停用词表.txt',encoding='utf-8')
stop_words = file_path.read()
# 删除停用词
# 新建一个空列表，用于存储删除停用词后的数据
new_data = []
for word in cut_words:
    if word not in stop_words:
        new_data.append(word)
new_data


# 词频统计
freq_list = FreqDist(new_data)
# 返回词语列表
most_common_words = freq_list.most_common()
most_common_words

# 导入所需要使用的包
from matplotlib import pyplot as plt
from wordcloud import WordCloud
# 词云显示
font = r'../mydata/STXINGKA.TTF'  # 华文行楷
wc = WordCloud(font_path = font, background_color = 'white',
               width = 1000, height = 800).generate(" ".join(new_data))
plt.imshow(wc)   # 用plt显示图片
plt.axis('off')  # 不显示坐标轴
plt.show()        # 显示图片






