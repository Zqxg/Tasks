# markdown学习笔记

## 学习背景
结合三件套（HTML+CSS+JavaScript）在浏览器上的执行逻辑，重新思考markdown的原理，写下我的新体验

## 学习内容的目录
1. [Markdown介绍](#1)
2. [工作原理](#2)
3. [Markdown和前端三件套](#3)
	+ markdown与html
	+ markdown与CSS
	+ markdown与JavaScript

## 学习内容
<p id="1"></p>

### 一、Markdown介绍

1. 设计灵感
主要来源于纯文本电子邮件的格式，目标是让人们能够使用易读、易写的纯文本格式编写文档，而且这些文档可以转换为HTML文档

2. Markdown相当于简化了的HTML，它只提供用户最常用的语法格式，更易读和易写，用户可以不必关心复杂的HTML标签，只专注于写作就行了

<p id="2"></p>

### 二、工作原理

 Markdown的工作流程很简单，首先要挑一款支持md格式的编辑器进行写作，内容使用Markdown进行标记，然后通过编辑器的功能将文章进行渲染、发布或导出。
![Markdown工作流程图](https://raw.githubusercontent.com/Zqxg/Tasks/main/images/Markdown%E5%B7%A5%E4%BD%9C%E6%B5%81%E7%A8%8B%E5%9B%BE.jpeg)
<p id="3"></p>

### 三、Markdown 与html、CSS、Js

#### （一） Markdown和html
Markdown应用程序将获取到的 Markdown 格式的文本输出为 HTML 格式（*将`*、# `等标记符号转换成相应的 HTML 标签*）

例如：（上为markdown、下为html）
```
# Heading 
## Sub-Heading 
This is a *paragraph*. 
>Quote.
```
 Markdown解释器将上面样式转换为下面样式
```
<h1>Heading</h1> 
<h2>Sub-Heading</h2> 
<p>This is a <em>paragraph</em>.</p> 
<blockquote><p>Quote.</p></blockquote>
```

#### （二）Markdown和CSS
由 CSS 决定 HTML 标签的外观表现，无论是段落行首缩进还是其他样式，都无法直接在 Markdown 中实现。只有更改用于配合输出 HTML 的 CSS 才能够实现

>比如< h1> 和 < h2> 的字号差异，都是由浏览器默认指定的 CSS 样式赋予的。如果将这些默认样式去除，那么各个标签并不会有外观上的差异。


#### （三） markdown和Js
1.  markdown文本最终要转换成HTML的格式，还是需要用marked.js这么一个库来解析。
2. 原理就是用ajax请求，取到 .md文件里的内容，再通过marked.js提供的marked()方法将markdown语法的文本转成html文档

![Markdown工作原理.png ](https://raw.githubusercontent.com/Zqxg/Tasks/main/images/Markdown%E5%B7%A5%E4%BD%9C%E5%8E%9F%E7%90%86-1.png)

## 参考资料
1. [(25条消息) 如何实现Markdown文件之间的跳转_icebird_craft的博客-CSDN博客_markdown跳转文件](https://blog.csdn.net/icestorm_rain/article/details/108991703)
2.  [(25条消息) markdown_页面中跳转_xieyan0811的博客-CSDN博客_markdown页面链接跳转](https://blog.csdn.net/xieyan0811/article/details/123978167)
3. [Markdown和HTML - 柠檬茶多放糖 - 博客园 (cnblogs.com)](https://www.cnblogs.com/yuguangtai/p/12858600.html)
4. [JS加载解析Markdown文档过程详解_javascript技巧_脚本之家 (jb51.net)](https://www.jb51.net/article/186851.htm)
