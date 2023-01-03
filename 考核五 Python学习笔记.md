#  Python学习笔记

## 学习内容的目录
1. [基础语法](#1)
2. [面向对象](#2)
3. [文件](#3)
4. [网络爬虫](#4)

## 学习内容
<p id="1"></p>

### 一、基础语法
#### （一）语法
1. 注释
Python中单行注释以 **#** 开头
多行注释可以用多个 # 号，或者 ''' 和 """
```
# 第一个注释 
# 第二个注释 
''' 
第三注释 
第四注释 
''' 
""" 
第五注释 
第六注释 
"""
```

2. 行与缩进
Python中不需要使用大括号 {}表示代码块，而是同一个代码块的语句必须包含相同的缩进空格数
```
if True: 
	print ("True") 
else: 
	print ("False")
```
>Python语法中没有分号，与c/c++不同

3.多行语句 
Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠 \ 来实现多行语句：
```
total = item_one + \
        item_two + \
        item_three
```
>在 [], {}, 或 () 中的多行语句，不需要使用反斜杠 \

4. 输入、输出
+ python 提供了 **input()** 内置函数从标准输入读入一行文本，默认的标准输入是键盘。
+ **print()** 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
```
# 不换行输出 
print( x, end=" " )
```
#### （二）基本数据类型
-   不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
-   可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合。

1. **Number**
+ Python3 支持 **int（整数）、float（浮点数）、bool（布尔）、complex（复数）**
+ 声名变量的格式：**变量名 = 值**
```
a = 5 #这里声明了一个变量a，并赋值为5
```
>python是弱类型的语言，变量的类型由其值的类型决定，不用为变量声名类型

+ 内置的 type() 函数可以用来查询变量所指的对象类型
+ 还可以用 isinstance 来判断
```
>>> a, b, c, d = 20, 5.5, True, 4+3j
>>> print(type(a), type(b), type(c), type(d))
>>> isinstance(a, int)
```

+ 数值运算
```
>>> 5 + 4  # 加法  
9  
>>> 4.3 - 2 # 减法  
2.3  
>>> 3 * 7  # 乘法  
21  
>>> 2 / 4  # 除法，得到一个浮点数  
0.5  
>>> 2 // 4 # 除法，得到一个整数  
0  
>>> 17 % 3 # 取余  
2  
>>> 2 ** 5 # 乘方  
32
```
> 1、Python可以同时为多个变量赋值，如a, b = 1, 2
> 2、一个变量可以通过赋值指向不同类型的对象。
   3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
   4、在混合计算时，Python会把整型转换成为浮点数。

2. **String**
Python中的字符串用单引号 `'` 或双引号`"`括起来
```
str = 'Runoob'  
  
print (str)          # 输出字符串  
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符  
print (str[0])       # 输出字符串第一个字符  
print (str[2:5])     # 输出从第三个开始到第五个的字符  
print (str[2:])      # 输出从第三个开始的后的所有字符  
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)  
print (str + "TEST") # 连接字符串
```
>与 C 字符串不同的是，Python 字符串不能被改变

3. List（列表）
列表的数据项不需要具有相同的类型,列表是一个有序且可更改的集合
+ 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可
```
list1 = ['Google', 'Runoob', 1997, 2000] 
list2 = [1, 2, 3, 4, 5 ] 
list3 = ["a", "b", "c", "d"] 
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
```
>索引与字符串类似

+ del 语句来删除列表的的元素
+ 列表都可以进行的操作包括索引，切片，加，乘，检查成员
+ 嵌套：
```
>>>a = ['a', 'b', 'c'] 
>>> n = [1, 2, 3] 
>>> x = [a, n] 
>>> x [['a', 'b', 'c'], [1, 2, 3]] 
>>> x[0] 
['a', 'b', 'c'] 
>>> x[0][1] 
'b'
```

+ 方法：
list.append(obj) 在列表末尾添加新的对象
list.count(obj) 统计某个元素在列表中出现的次数
list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.insert(index, obj) 将对象插入列表
等等

4. Dictionary（字典）
![字典](https://raw.githubusercontent.com/Zqxg/Tasks/main/images/%E5%AD%97%E5%85%B81.png)
字典用于储存键值对（key：value）


#### （三）函数
1. 语法
Python 定义函数使用 def 关键字（define的缩写）
```
def 函数名（参数列表）:
    函数体
    return
```

2. 参数传递
在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的
+ 不可更改的对象：strings, tuples, 和 numbers 
*变量赋值  **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a.*
+ 可修改对象： list,dict 等。
*变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了*

**python 传不可变对象:** 类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象

**传可变对象:** 
可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

#### （四）判断语句
1. if 条件控制
```
#如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
if condition_1:  
	statement_block_1 

#如果 "condition_1" 为False，将判断 "condition_2"
#如果"condition_2" 为 True 将执行 "statement_block_2" 块语句

elif condition_2: 
	statement_block_2 
	
#如果 "condition_2" 为False，将执行"statement_block_3"块语句
else: statement_block_3
```
>注1：Python 中用 **elif** 代替了 **else if**，所以if语句的关键字为：**if – elif – else**。
>注2：在 Python 中没有 switch...case 语句，但在 Python3.10 版本添加了 match...case，功能类似

2. match...case
```
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```
>注：`case _`: 类似于 C 和 Java 中的 default:，当其他 case 都无法匹配时，匹配这条，保证永远会匹配成功。

3. while循环
```
while 判断条件(condition)：
    执行语句(statements)……
```
+ while else
如果 while 后面的条件语句为 false 时，则执行 else 的语句块
```
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

4. for循环
```
for <variable> in <sequence>: 
	<statements> 
else: 
	<statements>
```
<p id="2"></p>

### 二、⾯向对象
#### （一）类
1. 类对象
类对象支持两种操作：属性引用和实例化。
```
class MyClass: 
	"""一个简单的类实例""" 
	i = 12345 
	def f(self): 
		return 'hello world' 
		
# 实例化类 
x = MyClass() 
# 访问类的属性和方法 
print("MyClass 类的属性 i 为：", x.i) 
print("MyClass 类的方法 f 输出为：", x.f())
```
2. 构造方法（类似c++的构造函数）
```
def __init__(self,其他属性):
```
>self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类

3. 方法
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
```
#类定义 
class people: 
	#定义基本属性 
	name = '' age = 0 
	#定义私有属性,私有属性在类外部无法直接进行访问 
	__weight = 0 
	#定义构造方法 
	def __init__(self,n,a,w): 
		self.name = n 
		self.age = a 
		self.__weight = w 
	def speak(self): 
	print("%s 说: 我 %d 岁。" %(self.name,self.age)) 
	
# 实例化类 
p = people('runoob',10,30) 
p.speak()
```

4. 类的属性
（1）私有属性：函数、方法或者属性的名称以两个下划线 `_` 开始，则为私有类型

+ `__attribute`：属性名前面加两个下划线，即声明该属性为私有，不能在类的外部直接访问，在类内部访问时用 `self.__attribute `。
+ `__function`：函数名前面加两个下划线，即声明该函数为私有，不能在类的外部直接访问，在类内部访问时用 `self.__function`。

（2）公有属性：如果函数、方法或者属性的名称没有以两个下划线开始，则为公有属性
（3）实例属性：以 `self` 作为前缀的属性
（4）局部变量：类的方法中定义的变量没有使用 `self` 作为前缀声明，则该变量为局部变量
>实例数据属性只能通过实例访问
>数据属性不需要预先定义，数据属性初次被使用时，即被创建并赋值

5. 类的专有方法
-   **__init__ :** 构造函数，在生成对象时调用
-   **__del__ :** 析构函数，释放对象时使用
-   **__repr__ :** 打印，转换
-   **__setitem__ :** 按照索引赋值
-   **__getitem__:** 按照索引获取值
-   **__len__:** 获得长度
-   **__cmp__:** 比较运算
-   **__call__:** 函数调用
-   **__add__:** 加运算
-   **__sub__:** 减运算
-   **__mul__:** 乘运算
-   **__truediv__:** 除运算
-   **__mod__:** 求余运算
-   **__pow__:** 乘方

#### （二）继承
继承允许我们定义继承另一个类的所有方法和属性的类。
父类：继承的类，也称为基类。
子类：从另一个类继承的类，也称为派生类。

1. 继承
在Python中，当一个子类只有一个父类时称为单继承。
```
# 子类定义
class 子类名(父类名):
```
>子类可以继承父类的所有公有成员和公有方法，但不能继承其私有成员和私有方法。

+ 在继承中基类的构造（`__init__()` 方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
+ 在调用基类的方法时，需要使用 super() 前缀。它会使子类从其父继承所有方法和属性
+ Python 总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找（先在本类中查找调用的方法，找不到才去基类中找）。
```
# 父类
class staff:  
    def __init__(self,n, i):  
        self.name = n  
        self.id = i

# 子类
class FullTimeEmployee(staff):  
    monthly_salary=0  
    def __init__(self,n,i,salary):  
        staff.__init__(self,n,i)  
        self.monthly_salary=salary
```
>子类的 `__init__()` 函数会覆盖对父的` __init__() `函数的继承。
如需保持父类的` __init__() `函数的继承，请添加对父的` __init__() `函数的调用

2. 多继承
多继承指一个子类可以有多个父类，它继承了多个父类的特性。多继承可以看作是对单继承的扩展，其语法格式如下：
```
#定义沙发父类  
class Sofa:  
	def printA(self):  
		print ('----这是沙发----')  
#定义床父类  
class Bed:  
	def printB(self):  
		print('----这是床----')  
  
#定义一个子类，继承自Sofa和Bed  
class Sofabed(Sofa,Bed):  
	def printC(self):  
		print('----这是沙发床----')
```
>在Python中，如果两个父类中有同名的方法，调用该同名方法时会调用先继承类中的方法


#### （三）模块
1. import语句
+ 先用import语句： import+模块名
+ 要使用模块的函数时： 模块名.函数名 或 模块名.变量名

2. from import语句
+ form+模块名 import +要使用的变量名（多个用逗号隔开）
> 好处：每次使用模块的函数时，不需要带上模块的名字

3. from import*
+ from+模块名 import* ：将模块内所有内容都引入
> 好处：同上
> 缺点：将所有函数和变量引入，引入多个模块可能产生冲突

<p id="3"></p>

### 三、文件
#### （一）文件定位
1. 绝对路径：
+ Windows系统：以分区名＋反斜杠`\`开头，中间用反斜杠分隔，目标目录结尾
+ 类Unix系统：以斜杠`/`开头，中间用斜杠分隔，最后用目标文件或目标目录结尾
2. 相对路径：
+ 用`.`表示当前目录，`..`表示上一层父目录

#### （二）读取文件
1. 打开目标文件：open()函数
open("目标文件路径"，"模式")
>有四种打开文件的不同方法（模式）：
>`"r"` - 读取 - 默认值。打开文件进行读取，如果文件不存在则报错。
>`"a"` - 追加 - 打开供追加的文件，如果不存在则创建该文件。
>`"w"` - 写入 - 打开文件进行写入，如果文件不存在则创建该文件。
>`"x"` - 创建 - 创建指定的文件，如果文件存在则返回错误。

2. 读取：read() 
`read()` 方法用于读取文件的内容，默认情况下，`read()` 方法返回整个文本
```
f = open("demofile.txt", "r")
print(f.read())
```
>注：当文件很大的时候，最好不要使用read，会占用很大内存，可以指定要读取的字符数
```
f = open("demofile.txt", "r")
print(f.read(10)) # 会读第1-10个字节的文件内容
print(f.read(10)) # 会读第11-20个字节的文件内容
```

3. 读行：readline()方法
读取文件中的一行
```
f = open("demofile.txt", "r")
print(f.readline())
```
>通过循环遍历文件中的行，您可以逐行读取整个文件

4. 关闭文件：close()
打开文件后，要及时关闭文件
```
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

>使用with open("文件路径") as 对象名: 操作 缩进的操作完成后，文件会自动关闭

#### （三）文件写入/创建
1. 写入已有文件
+ `"a"` - 追加 - 会追加到文件的末尾
+ `"w"` - 写入 - 会覆盖任何已有的内容
追加:
```
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

# 追加后，打开并读取该文件：
f = open("demofile2.txt", "r")
print(f.read())
```

覆盖：
```
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

# 写入后，打开并读取该文件：
f = open("demofile3.txt", "r")
print(f.read())
```

2. 创建新文件
 Python 中创建新文件，请使用 `open()` 方法，并使用以下参数之一：
-   `"x"` - 创建 - 将创建一个文件，如果文件存在则返回错误
-   `"a"` - 追加 - 如果指定的文件不存在，将创建一个文件
-   `"w"` - 写入 - 如果指定的文件不存在，将创建一个文件

#### （四） 文件删除
1. 如需删除文件，必须导入 OS 模块，并运行其 `os.remove()` 函数：
```
# 删除文件 "demofile.txt"：
import os
os.remove("demofile.txt")
```

2. 检查文件是否存在
检查文件是否存在，然后删除它：
```
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

3. 删除文件夹：使用 `os.rmdir()` 方法
```
#删除文件夹 "myfolder"：
import os
os.rmdir("myfolder")
```


<p id="4"></p>

### 四、网络爬虫
#### （一）入门
通过程序来爬取互联网上的优秀资源(图片、音频、视频、数据)
需求：用程序模拟浏览器，输入一个网址，从该网址中获取到资源或者内容

1. 引入网址模块
from urllib.request import urlopen
>urllib 库 是 Python内置的 HTTP 请求库。其中urllib.request 是请求模块
>urllib.request 模块提供了最基本的构造 HTTP （或其他协议如 FTP）请求的方法，利用它可以模拟浏览器的一个请求发起过程。利用不同的协议去获取 URL 信息。

**urlopen:**
```
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
```
>参数说明：
>url:需要打开的网址 
>data: Post 提交的数据, 默认为 None ，当 data 不为 None 时, urlopen() 提交方式为 Post timeout：设置网站访问超时时间

2. 读取内容
+ 用read()读取urlopen后的内容
+ 将字节转换为字符串:对象名.read().decode("gdk或utf-8") *具体操作看浏览器*

3. 将内容保存到文件
将页面html源代码保存到我们自定义的文件内

#### （二）Web请求过程
1. 服务器渲染：在服务器那边直接将数据与html整合一起，统一返回给浏览器
+ 在页面源代码中，能看到数据
2. 客户端渲染：
+ 第一次请求只要一个html骨架，第二次请求拿到数据，进行数据展示
+ 在页面源代码中，看不到数据
#### （三）http协议
http协议把一条消息分为三大块内容，无论是请求还是响应都是三块内容
1. 请求：
```
请求行 -> 请求方式(get/post) 请求url地址 协议
请求头 -> 放一些服务器要使用的附加信息

请求体 -> 一般放一些请求参数
```

2. 响应：
```
状态行 -> 协议 状态码（例如：404）
响应头 -> 放一些客户端要使用的一些附加信息

响应体 -> 服务器返回的真正客服端要用的内容(html，json等)
```
>写爬虫的时候要格外注意请求头和响应头

+ 请求头中最常见的一些重要内容(爬虫需要)：
	+ 1.User-Agent：请求载体身份标示(用啥发送的请求)
	+ 2.Referer:防盗链(这次请求是从哪个页面来的？反爬会用到)
	+ 3.cookie:本地字符串数据信息(用户登录信息，反爬的token)
+ 响应头中一些重要内容：
	+ 1.cookie：本地字符串数据信息(用户登录信息，反爬的token)
	+ 2.各种神奇的莫名其妙的字符串

3. 请求方式
+ GET:显示提交
+ POST:隐式提交 发送post请求，发送的数据必须放在字典中，通过data参数进行传递

#### （四）Requests模块入门
该模块主要用来发 送 HTTP 请求，requests 模块比 urllib 模块更简洁
1. 安装模块：在pycharm中添加软件包
2. 导入模块：import requests
3. 发送请求和获得响应：resp=requsts.get(url) 
4. 拿到页面源代码: resp.text
>如果请求失败，可以试着修改请求头绕过反爬
## 参考资料
1. [[1] 120分钟入门Python | 超超基础入门课程预告_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1hf4y1u7CH/?spm_id_from=333.788&vd_source=83dd43e74255c7f8534d577021ce91a6)
2. [类_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV16A411i7W7?p=6&spm_id_from=pageDriver&vd_source=83dd43e74255c7f8534d577021ce91a6)
3. [Python3 面向对象 | 菜鸟教程 (runoob.com)](https://www.runoob.com/python3/python3-class.html)
4. [Python 迭代器 (w3school.com.cn)](https://www.w3school.com.cn/python/python_iterators.asp)
5. [python3中urllib库的request模块详解 - lincappu - 博客园 (cnblogs.com)](https://www.cnblogs.com/lincappu/p/12762771.html)
6. [1 3 手刃一个小爬虫（下）_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1rv4y1K7yV/?p=4&spm_id_from=pageDriver&vd_source=83dd43e74255c7f8534d577021ce91a6)
7. [(31条消息) PyCharm中安装requests库_技术人小柒的博客-CSDN博客_pycharm安装requests](https://blog.csdn.net/m0_46983541/article/details/121181688)
8. [(31条消息) Python爬取网页源码，图片和文字到本地_苦涩精灵的博客-CSDN博客](https://blog.csdn.net/weixin_43873198/article/details/107461941)