'''
Python 使用 SAX 解析 xml
'''
# SAX 是一种基于事件驱动的API。
# 利用 SAX 解析 XML 文档牵涉到两个部分: 解析器和事件处理器。
# 解析器负责读取 XML 文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
# 而事件处理器则负责对事件作出响应，对传递的 XML 数据进行处理。
# 1、对大型文件进行处理；
# 2、只需要文件的部分内容，或者只需从文件中得到特定信息。
# 3、想建立自己的对象模型的时候。
# 在 Python 中使用 sax 方式处理 xml 要先引入 xml.sax 中的 parse 函数，还有 xml.sax.handler 中的 ContentHandler。
# make_parser 方法
# 以下方法创建一个新的解析器对象并返回。
# xml.sax.make_parser( [parser_list] )
# 参数说明:
# parser_list - 可选参数，解析器列表
# parser 方法
# 以下方法创建一个 SAX 解析器并解析xml文档：
# xml.sax.parse( xmlfile, contenthandler[, errorhandler])
# 参数说明:
# xmlfile - xml文件名
# contenthandler - 必须是一个 ContentHandler 的对象
# errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX ErrorHandler 对象
# parseString 方法
# parseString 方法创建一个 XML 解析器并解析 xml 字符串：
# xml.sax.parseString(xmlstring, contenthandler[, errorhandler])
# 参数说明:
# xmlstring - xml字符串
# contenthandler - 必须是一个 ContentHandler 的对象
# errorhandler - 如果指定该参数，errorhandler 必须是一个 SAX ErrorHandler对象

'''Python解析XML实例
# !/usr/bin/python3
'''

import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 元素开始调用
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            print("*****Movie*****")
            title = attributes["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, tag):
        if self.CurrentData == "type":
            print("Type:", self.type)
        elif self.CurrentData == "format":
            print("Format:", self.format)
        elif self.CurrentData == "year":
            print("Year:", self.year)
        elif self.CurrentData == "rating":
            print("Rating:", self.rating)
        elif self.CurrentData == "stars":
            print("Stars:", self.stars)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # 读取字符时调用
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")

'''
使用xml.dom解析xml
文件对象模型（Document Object Model，简称DOM），是W3C组织推荐的处理可扩展置标语言的标准编程接口。
一个 DOM 的解析器在解析一个 XML 文档时，一次性读取整个文档，把文档中所有元素保存在内存中的一个树结构里，之后你可以利用DOM 提供的不同的函数来读取或修改文档的内容和结构，也可以把修改过的内容写入xml文件。
python中用xml.dom.minidom来解析xml文件，
'''
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print ("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print ("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print ("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print ("Description: %s" % description.childNodes[0].data)