# Python爬虫笔记

## 学习内容的目录
1. [获得网址源文件](#1)
2. [解析源文件](#2)
3. [遇到的问题和解决](#3)

## 学习内容
<p id="1"></p>

### 一、获得网址源文件
#### （一）requests模块
1. 引入requests模块
2. 发生请求和获得响应
3. 得到网址的源文件

#### （二）Beautiful Soup4库安装和使用
Beautiful Soup 是一个可以从 HTML 或 XML 文件中提取数据的 Python 库.
1. 安装Beautiful Soup库

2. 安装lxml库
使用方法:BeautifulSoup(markup, “lxml”）


#### （三）获取
1. 获取网址
+ 打开geek招新网站，f12复制网址，并发现使用的是get请求
+ 为了防止被拦截，复制浏览器中的请求头
2. 发送请求和获取
```
res = requests.get(url,headers=headers)  
res.encoding = 'utf-8'  
soup = BeautifulSoup(res.text,'lxml')
```
<p id="2"></p>

### 二、解析源文件
#### （一）保存图片
1. 获取图片
```
imgs = soup.find_all('img')
```
2. 使用for循环获取图片网址
```
	img_url = url + i['src'][1:]
```
3. 调用定义好的保存图片方法get_pic()
+ 使用os模块设置文件路径
+ 判断**是否存在：os.path.exists()**，没有就**新建：os.mkdir() 方法**
+ 使用content用于获取图片
+ 写入图片
>因为图片是二进制的，使用要使用wb写入图片
#### （二）保存文字
1. 获取文字
```
elm_a = soup.find_all('a',attrs={'id':'QA-a'})  
elm_p = soup.find_all('p')
```
>attrs属性:在find_all()方法中，发现要获取的文字有id属性，使用attrs来获取

2. 使用循环，调用定义好的保存文字方法get_pic()
+ 使用os模块设置文件路径
+ 判断**是否存在：os.path.exists()**，没有就**新建：os.mkdir() 方法**
+ 写入文字
<p id="3"></p>

### 三、遇到的问题和解决
#### （一）环境适配
1. 版本问题:
一开始下载的是python 3.11.1版本，发现代码运行不了，反复报错。重新下载3.7.8版本的python，适配需要的包。

2. 解释器路径：
修改解释器路径，并重新安装各种需要的包

#### （二）网络问题
1. 网络连接问题
使用家里WiFi无法正常进入官网，改用手机流量后成功进入，可能是路由器有问题

#### （三）其他问题
1. 报错：bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
+ 使用 pip install lxml 安装，安装完后，在运行还是一样出错
+ 经百度、知乎的说法是新的库不支持，新版本语法支持改变了，在报错代码中把函数参数中所有的"lxml"改成"html.parser"

## 参考资料
1. [(31条消息) 使用Requests库和BeautifulSoup库来爬取网页上需要的文字与图片_就爱跑步喝可乐的博客-CSDN博客](https://blog.csdn.net/wanghaoranand/article/details/76944560?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-76944560-blog-113672543.pc_relevant_3mothn_strategy_recovery&spm=1001.2101.3001.4242.1&utm_relevant_index=3)
2. [python如何爬取网页中的文字 (51sjk.com)](https://www.51sjk.com/b70b307343/)
3. [Python 高效提取 HTML 文本的方法 (qq.com)](https://mp.weixin.qq.com/s?__biz=MzAxMjUyNDQ5OA==&mid=2653569257&idx=1&sn=c4415fce968b6cf707a8cfcf0bf7d3e5&chksm=806e6e54b719e7425982fa3ce28115489b3c7b43f5c1a343185396846eeda4bf3b16c9eef1a9&scene=27)
4. [自然语言处理实验演示 - 50. 提取 HTML 标记文本_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1b34y1m7wR/?spm_id_from=333.337.search-card.all.click&vd_source=83dd43e74255c7f8534d577021ce91a6)
5. [BeautifulSoup的基本用法 - 宇宙刘 - 博客园 (cnblogs.com)](https://www.cnblogs.com/yuzhouliu/p/16075636.html)
6. https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html