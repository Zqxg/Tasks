# Geek网站复刻笔记


## 目录
1. 导航栏
	+ [导航栏样式](#1.1)
	+ [导航栏功能](#1.2)
	+ [回到顶部](#1.3)
2. 图片
	+ [设置背景图片](#2.1)
	+ [Geek图标放大](#2.2)
	+ [文字和图片左右排布](#2.3)
	+ [图片旋转](#2.4)
	+ [图片对称](#2.5)
	+ [靠近蝴蝶](#2.6)
3. 盒子
	+ [盒子阴影](#3.1)
	+ [div边框高度随内容改变而变化](#
4. 按钮
	+ [button按钮的外边框隐藏](#1.1)
	+ [按钮点击复制文本到剪贴板](#1.1)
5. 文本
	+ [Contact Us里的文本前面带小黑点](#5.1)
	+ [Q&A中显示、隐藏文字](#5.2)
	+ [图标文字](#5.3)
6. [移动端适配](#6)
7. [待改进问题](#7)

## 复刻的内容
<p id="1"></p>

### 一、导航栏
<p id="1.1"></p>

#### （一）导航栏样式
1. 使用无序列表设置导航栏

2. 使用css修改无序列表样式
+ 修改浮动样式float标签
+ 修改字体、背景、透明度opacity

3. 将导航栏和文字居中

<p id="1.2"></p>

#### （二）导航栏功能
1. 导航栏固定、导航栏显示
使用position: fixed;将导航栏固定，随后发现下方的背景图片直接将导航栏覆盖，修改下方背景图片的top值。然后设置导航栏的z-index比背景图片的大。

2. 导航栏下拉功能
+ 确定位置，内容。将下拉图片使用div包裹，放到introduction位置下。
+ 修改图片display属性，让它默认为none
+ 使用鼠标悬停功能，当鼠标移动到introduction位置，改变图片display实现导航栏下拉功能。

3. 导航栏转跳**页面内**某位置
使用js点击事件，实现定位跳转功能。
```
function jump1(){	 
    document.getElementById("introduction").scrollIntoView(true);
}
```
>scrollIntoView() 方法让当前的元素滚动到浏览器窗口的可视区域内。

4. 导航栏转跳**其他页面**
使用js点击事件，实现定位跳转功能。
```
function jump3(){
	window.open("https://campus.new-thread.com/")
}
```
>window.open(URL)  ：  在一个新的窗口打开一个新的页面
>window.location.href=URL ： 在本窗体打开一个新的页面，也是最常用的一种方法
>location.replace(URL) ：本窗口的页面被替换为一个新的页面URL，替换后不可以回退到上个页面


<p id="1.3"></p>

#### （三）回到顶部
想法：将两个图标竖向排列，溢出的图标2部分隐藏，然后鼠标悬停后，图标同时上移，图标1溢出隐藏，图标2显示。
1. 鼠标悬停改变图标位置 ，使用transform: translate(x,y)达到位置移动
2. 使用鼠标点击事件，scrollIntoView() 方法实现跳转

### 二、图片
<p id="2.1"></p>

#### （一）设置背景图片
1. 设置背景图片大小
直接将图片放上去，会导致背景图片过大，需要修改图片的参数。
2. 修改图片位置
将Geek图标移到背景中间

<p id="2.2"></p>

#### （二）Geek图标放大
1. 将中间的Geek图标变成原来的35%
2. 设置鼠标悬停效果
鼠标移到Geek图标后，将图标变成修改后的1.4倍
3. 增加过渡效果

<p id="2.3"></p>

#### （三）文字和图片左右排布
1. 将文字和图片用一个div包裹
2. 再用一个div包裹文字
3. 使用弹性盒子布局，实现文字和图片左右布局

<p id="2.4"></p>

#### （四）图片旋转
1. 设置鼠标悬停效果，然后使用transform属性使图片旋转
```
transform: rotate(旋转角度deg)
```
2. 使用transition属性添加过渡动画效果

<p id="2.5"></p>

#### （五）图片对称
1. transform属性通过rotateY让图片在Y轴旋转180度，从而实现图片沿Y轴对称
2. 同理rotateX让图片在X轴旋转180度，从而实现图片沿X轴对称

<p id="2.6"></p>

#### （六）靠近蝴蝶
1. 显示文字
和导航栏下拉类似，都是现将文字隐藏，然后鼠标靠近后修改display属性，显示文字出来
+ 1、给文字元素添加“display:none;”样式使其隐藏；
+ 2、使用“父元素:hover 文字元素{display:block;}”语句实现鼠标放在图片上显示文字的效果。

2. 蝴蝶移动
和introduction的文本框放大类似，都是使用鼠标悬停效果，鼠标靠近图片后改变蝴蝶的位置，实现蝴蝶上下移动效果。

<p id="3"></p>


### 三、盒子
<p id="3.1"></p>

#### （一）盒子阴影
使用box-shadow属性给边框增加阴影特效
+ box-shadow属性:
	+ h-shadow 水平阴影的位置。 **必需的**
	+ v-shadow 垂直阴影的位置。 **必需的**
	+ blur 模糊距离 (可选)
	+ spread 阴影的大小 （可选）
	+ color 阴影的颜色 （可选）
	+ inset 从外层的阴影（开始时）改变阴影内侧阴影 （可选）
```
box-shadow: h-shadow v-shadow blur spread color inset;
```
![盒子阴影.png (1571×812) (raw.githubusercontent.com)](https://raw.githubusercontent.com/Zqxg/Tasks/main/images/%E7%9B%92%E5%AD%90%E9%98%B4%E5%BD%B1.png)

<p id="3.2"></p>

#### （二）div边框高度随内容改变而变化
问题：在写Q&A模块的时候，一开始在大div里面插入图片，然后设置溢出隐藏。后来发现这样问题也会消失，就在离图片最近的div设置溢出隐藏。结果发现随着答案的显示，超过最外层边框，想要实现div边框高度随内容改变而变化。

1. 将图片为设置div背景，使用background-image属性
```
background-image: url("图片路径");
```
2. 设置div的最小高度min-height，既保证文本超出边框前的美观，又实现了div边框高度随内容改变而变化的功能

### 四、按钮
<p id="4.1"></p>

#### （一） button按钮的外边框隐藏
使用border-style属性将按钮的外边框设置为空
```
border-style: none;
```

<p id="4.2"></p>

#### （二）按钮点击复制文本到剪贴板
用textare标签来保存文本，然后使用js的点击事件，点击复制。
1. 用`<textarea>`存储文本，设置id，和对应的按钮放在同一个div下
```
<textarea row="3" cols="20"> 
	文本内容
</textarea>
```
>row：显示的行数，cols：每行中的字符数

2. 在对应的button中设置点击事件copy()函数
3. 在copy()中，选择文本对象，然后执行浏览器复制命令，最后弹出警示框
```
function copy1(){
	var u1=document.getElementById("qqgroup");
	u1.select();// 选择对象
	document.execCommand("Copy");// 执行浏览器复制命令
	alert("小锅温馨提示：QQ群号复制到剪贴板了哦 Y^-^Y");
}
```
>`<input>`和`<textarea>`两种文本框都支持select()方法，Textarea 对象的 **select()** 方法用于选择该元素中的文本。


### 五、文本
<p id="5.1"></p>

#### （一） Contact Us里的文本前面带小黑点
使用li标签代替p标签，使文本前面自带小黑点

<p id="5.2"></p>

#### （二）Q&A中显示、隐藏文字
功能：第一次点击问题，显示答案文字；再次点击，答案文字隐藏。
1. 将问题和回答放到一个div下，然后设置回答文字的display属性，使其隐藏
2. 然后在问题文字那边，设置一个点击事件
3. js中通过if条件判断css样式，如果是隐藏的点击后就显示，如果是显示的点击后就隐藏。
```
function show1(){
	let show = document.querySelector(".answer1");
	if(show.style.display=="none"){
		show.style.display="block";
	}else{
		show.style.display="none";
	}
}
```

<p id="5.3"></p>

#### （三）图标文字
1. 将Font Awesome加入网页中
```
<link rel="stylesheet" href="https://cdn.staticfile.org/font-awesome/4.7.0/css/font-awesome.css">
```
2. 在Font Awesome官网中找到需要的图案，复制代码粘贴到所需位置

<p id="6"></p>

### 六、移动端适配
1. 最先要让页面尺寸布满显示屏又不可以外溢，使用viewport标签：网页默认的宽度和高度，使网页宽度默认等于屏幕宽度
```
<meta name="viewport" content="width=device-width,maximum-scale=1.0, minimum-scale=1.0, user-scalable=no">
```
>使用上面属性的例子时，视口的宽度与屏幕的宽度相等，用户打开该页面时不需要横向拖动页面，即可看清页面展示的内容。

2. 将绝对宽度都改成**百分比**形式
3. 字体大小随边框改变。在css中，可以利用**vw单位**来实现让文字自动改变大小。
4. 中间geek的logo图片位置相对不变，完成缩放
5. **响应式div边框**：
一开始修改的时候，遇到很多问题。*修改最外层div的position属性后，有的文本内容超过最外层边框了。*
+ 修改position属性后，其他元素的位置也发生变化，需要修改内层元素的位置
+ 高度应该设置为auto，让高度随内容变化而变化

>一开始没改position的时候，发现将浏览器形状改变，后面的文本会将前面的部分文本覆盖，所以将position都重新修改了一边，问题解决了

6. 上传第一次代码，用手机端查看，发现文字大小有问题，于是将字体vh单位改vw单位

<p id="7"></p>

### 七、待改进问题
1. 发现Q&A的每个问题第一次点击失效，第二次及以上点击才可以显示答案
2. 导航栏NewThread文本后面无法加图标？有些图标无法正常显示
3. 手机端的about us界面最下面的三个按钮位置溢出
4. 手机端的返回顶部按钮形状问题,和上移问题