2023-11-26
今日学习内容：git简单命令。
克隆仓库：git clone
已经在仓库中（且有权限）之后：
添加：git add 
提交：git commit -m xxxx
查看状态：git status 

拉取最新：git pull 
推送最新：git push  

查看日志：git log

2023-11-27

今日学习内容：git简单命令复习

使用cmd在终端更新ssh-keygen，克隆仓库：git clone

未学习内容：api请求

**2023-11-28**

**URL是什么？**

 **1.**URL是“统一资源定位符”（Uniform Resource Locator）的首字母缩写，简单理解为“网址” 即可。

示例：

<link href="css/style.css" rel="stylesheet">

（1）href的含义是指属性指定链接资源的URL。URL可以是绝对的也可以是相对的路径。

（2）rel是指此属性命名链接文档与当前文档的关系。注意**这个属性必须是由空格分隔的链接类型值列表。**

# **HTML 相关知识**

##  **1.**HTML基础

（1）标题（Heading）是通过<h1> - <h6> 标签来定义的。

 示例：

 <h1>
     这是一个标题
 </h1> 

（2） 段落是通过标签 <p> 来定义的。

 示例：

 <p>
     这是一个段落。
 </p>  

（3） 链接是通过标签 <a> 来定义的 。

 示例：

<a href="https://www.runoob.com">

这是一个链接

</a>

 （4）图像是通过标签 <img> 来定义的。

示例：

<img src="/images/logo.png" width="258" height="39" />

 注释： (src)图像的名称和(width ,heigt)尺寸是以属性的形式提供的。

(5)  没有内容的 HTML 元素被称为空元素, 是通过<br>来定义的。

（<br>标签定义换行）。 如果希望不产生一个新段落的情况下进行换行（新行） ，也使用<br>

**特别的**， 对于 HTML，我们无法通过在 HTML 代码中添加额外的空格或换行来改变输出的效果。 

  <br> <br/>  <br />

上述三个写法都可以，注意不存在 </br>  写法。 

## **2.**HTML属性

（1） 属性总是以名称/值对的形式出现，**比如：name="value"** ，类似于键值对。

注释：属性值应该始终被包括在引号内。

双引号是最常用的，不过使用单引号也没有问题。**特别的**， 属性值本身就含有双引号，那么必须使用单引号。

**总结：**（1） class 属性可以多用 class=" " （引号里面可以填入多个class属性）  

（2） id 属性只能单独设置 id=" "（只能填写一个，多个无效） ，具有唯一性。

**3.**HTML标题

（1）HTML 水平线 ，<hr> 标签在 HTML 页面中创建水平线。  hr 元素可用于分隔内容 。

（2）HTML 注释， 将注释插入 HTML 代码中 ，

示例：

<!-- 这是一个注释 -->



##  **3.**HTML文本格式化![image-20231128115718620](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231128115718620.png)

![image-20231128115922683](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231128115922683.png)

![image-20231128120150693](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231128120150693.png)



（1）<q>指的是定义一个短的引用语，quote

​          <blockquote>指的是定义一个短的引用语  ,

(2)<dfn>指的是定义一个定义项目。

## **2023-11-29**

 **HTML链接**

<a href="https://www.runoob.com/">访问菜鸟教程</a>

 上面这行代码显示为：[访问菜鸟教程](https://www.runoob.com/) ， 点击这个超链接会把用户带到菜鸟教程的首页 。

 **文本链接：**最常见的链接类型是文本链接，它使用 <a> 元素将一段文本转化为可点击的链接 ： 如上所示

 **图像链接：**您还可以使用图像作为链接。在这种情况下，<a> 元素包围着 <img> 元素。 

示例：

<a href="https://www.example.com">
  <img src="example.jpg" alt="示例图片">
</a>

 **锚点链接：**除了链接到其他网页外，您还可以在[同一页面内创建内部链接]()，这称为锚点链接。要创建锚点链接，需要在目标位置使用 <a> 元素定义一个标记，并使用#符号引用该标记。 

示例：

<a href="#section2">跳转到第二部分</a>
<!-- 在页面中的某个位置 -->
<a name="section2"></a>

 **下载链接：**如果希望链接用于下载文件而不是导航到另一个网页，可以使用 download 属性。  

示例：

<a href="document.pdf" download>下载文档</a>

 **HTML头部**

head与header的区别

 head 标签用于定义文档头部，它是所有头部元素的容器 。

 head 元素可以引用脚本、指示浏览器在哪里找到样式表、提供元信息等等。 

示例：

<head>

  <title>

​    Van Gogh

  </title>

  <link href="css/style.css" rel="stylesheet">

</head>

- [x] 链接外部的css样式库

header 标签用于定义文档的页眉（介绍信息）。 

 **CSS** (Cascading Style Sheets) 用于渲染HTML元素标签的样式 

***内部样式表***

 当单个文件需要特别样式时，就可以使用内部样式表。你可以在<head>  部分通过 <style>标签定义内部样式表 

示例：

<head>
<style type="text/css">
body {background-color:yellow;}
p {color:blue;}
</style>
</head>

***外部样式表***

 当样式需要被应用到很多页面的时候 ， 可以通过更改一个文件来改变整个站点的外观。 

示例：

<head>
<link rel="stylesheet" type="text/css" href="mystyle.css">
</head>

### CSS 引入外部标签

通常使用 link,相较于import更加稳定。

<link rel="stylesheet" href="标签路径">

- [x] 本质的差别：**link** 属于 XHTML 标签，而 @import 完全是 CSS 提供的一种方式。 

  #### **HTML列表**

  

  ul是unordered lists的缩写 (无序列表)

  li是list item的缩写 （列表项目）

  ol是ordered lists的缩写（有序列表）

  dl是definition lists的英文缩写 (自定义列表)

  dt是definition term的缩写 (自定义列表组)

  dd是definition description的缩写（自定义列表描述）

  nl是navigation lists的英文缩写 （导航列表）

  tr是table row的缩写 （表格中的一行）

  th是table header cell的缩写 （表格中的表头）

  td是table data cell的缩写 （表格中的一个单元格）

  ## **2023-11-30**

  #### **HTML区块**

   通过 <div> 和 <span>将元素组合起来 。

 <div> 元素是块级元素，它可用于组合其他 HTML 元素的容器  

 <span> 元素是内联元素，可用作文本的容器 

 **块级元素 与 行内元素 的区别**

 div   默认样式为块级显示 ， 可以容纳其他块级元素和行内元素 ，

 <!--用于创建页面结构和布局--> 

span  默认样式为行内显示 ， 用来包裹文本或其他行内元素 ，比如用来设置特定的文本样式，

 <!--用于对文本或行内元素进行样式化或包裹--> 

####    HTML表单

 （1）收集用户的输入信息 。

 （2） 表示文档中的一个区域，这个区域包含交互控件，将用户收集到的信息发送到 Web 服务器。

 （3） 通常包含各种输入字段、复选框、单选按钮、下拉列表等元素 。

使用 form来创建表单

可以在表单找那个输入以下内容：

------



1. 文本域（textarea） , 下拉列表（select）、单选框（radio-buttons）、复选框（checkbox） 等等。 

表单的输入元素

（1） 输入标签 <input> 

（2） 输入类型是由 **type** 属性定义 

​       **常用的输入类型** 

- [x] ​        ***文本域***:    <input type="text"> 

- [x] ​        ***密码字段***: <input type="password"> 

- [x] ​        ***单选按钮***： <input type="radio"> 可以设置以下几个属性： 

name: 为控件命名，以备后台程序 ASP、PHP 使用 

value: 提交数据到服务器的值

checked : 当设置 [checked="checked"]() 时，该选项被默认选中 

示例：

<form>
<p>你生活在哪个国家？</p>
<input type="radio" name="country" value="China" checked="checked">中国<br />
<input type="radio" name="country" value="the USA">美国
</form>

**注意**： 同一组的单选按钮，name 取值一定要一致 

- [x] ​        ***复选框***： <input type="checkbox"> 

- [x] ​        ***提交按钮***: <input type="submit"> 

####  HTML脚本

 JavaScript 使 HTML 页面具有更强的动态和交互性 

 <script>  

（1）标签用于定义客户端脚本，比如 JavaScript 

 （2）元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件 

 （3）JS最常用于图片操作，表单验证，内容动态更新

当浏览器不能使用脚本的时候，使用 <noscript> 标签

#### HTML字符实体

**lt** : less than     表示  < 

**gt** : greater than    表示   \> 

**amp** : ampersand     表示   & 

**quot** : quotation      表示  " 

详见下图：

![image-20231130153231217](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231130153231217.png)



### 文本格式化（Formatting）

<b>粗体文本</b>
<code>计算机代码</code>
<em>强调文本</em>
<i>斜体文本</i>
<kbd>键盘输入</kbd> 

<pre>预格式化文本</pre>
<small>更小的文本</small>
<strong>重要的文本</strong>

<abbr> （缩写）

<address> （联系信息）
<bdo> （文字方向）
<blockquote> （从另一个源引用的部分）
<cite> （工作的名称）
<del> （删除的文本）
<ins> （插入的文本）
<sub> （下标文本）
<sup> （上标文本）

### 链接（Links）

 ![image-20231130201947170](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231130201947170.png)



## **2023-12-1**

了解api请求的调用

- [x] 1.GET与POST

- [x] 2.阅读简单的天气查询py文件代码

- [x] 3.改写快递查询py文件代码

- [ ] 4.学习相关的HTML快递查询html文件代码编写

  



