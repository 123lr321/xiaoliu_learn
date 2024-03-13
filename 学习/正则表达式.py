#
r"""
match（pattern，str）:只匹配开头，不成功返回none
search（pattern，str）：全文搜索，（只找一个）
findall（pattern，str）：全文搜索，（找寻全部）
sub（r'正则表达式’，’新内容‘，string）=替换内容（新内容也可以是一个函数）
split(r'正则表达式’，需分割内容）=分割后的列表
span:返回位置
group：提取匹配内容
s
.任意字符
^开头
$结尾
【】范围
{，}数量控制
\s 空白（空格）
\b 边界（非空与空格的边界）
\d 数字
\w 字母+数字
| 或者（word1|word2|word3）（区别（【word1word2word3】
!!!!!
python中\被视为转义字符，字符转义优先级高于正则，因此所以需要在’之前加r，or输入两个\\，例若想正则\w需输入\\w or r‘\w'
若相匹配\则需输入\\\\or r'\\',同类，若想匹配单.则是输入\\.，两个\经过字符转义变成一个\，一个\在正则转义中令。变成了单。
量词
!!!
python总是默认贪婪，总想要匹配更多的字符，如果想要非贪婪就在量词{}+*？后加？，就将贪婪转成非贪婪，
* 》=0
+ 》=1
？ 0 or 1
{m} 固定m位
{m，}》=m
{m，n} 》=m and 《=n
|等于或，若想将搜索结果分组，则需要在正则里面加（）用group将搜索结果分组展示
正则表达式里也可引用分组
分组也可以起名（？P<名字>正则表达式）
无名引用按顺序\1 \2等
有名按（？P=名字）

"""
import re

# 正确写法
# 满足qq格式
qq = '1875281348'
result = re.match('^[1-9][0-9]{4,9}$', qq)
print(result)
# 满足用户名（字母数字6位以上，不能数字开头）
username = 'l1323123'
result = re.search('^[\\w]\\d{5,}$', username)
print(result)
# 匹配文件
msg = 'a*py bb.png cc.doc dd.py'
result = re.findall('[a-z]{1,}\\.py', msg)
print(result)
# 爬虫|=或，分组表示需要在正则里面加（）
phone = '010-12345678'
result = re.match(r'(\d{3}|\d{4})-(\d{8})$', phone)
print(result.group(1))
# 引用
msg = '<html><h1>abc<html>'
result = re.match(r'<(\w+)+>(.+)<\1>$', msg)
print(result.group(

))
msg = '<html><h1>abc<h1><html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)<(?P=name2)><(?P=name1)>$', msg)
print(result.group())


def func(temp):
    return str(int(temp.group()) + 1)


result = re.sub(r'\d+', func, 'xuy:100,liur:110')
result1 = re.sub(r'\d+', '111', 'xuy:100,liur:110')
result2 = re.split(r'[,:]', 'xuy:100,liur:110')
print(result, result1,result2)
