Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
 
  File "<pyshell#0>", line 2
    y='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
    ^
IndentationError: unexpected indent
>>> y ='123@qq.comaaa@163.combbb@126.comasdfasfs33333@adfcom'
>>> import re
>>> re.findall('\w+@(qq|163|126).com', y)
['qq', '163', '126']
>>> re.findall('\w+@(?:qq|163|126).com', y)
['123@qq.com', 'aaa@163.com', 'bbb@126.com']
>>> y = 'tel:010-12345678 address:changanRoad'
>>> re.findall('\d', y)
['0', '1', '0', '1', '2', '3', '4', '5', '6', '7', '8']
>>> re.findall('\d+', y)
['010', '12345678']
>>> re.findall('\d+-', y)
['010-']
>>> re.findall('\d+-\d+', y)
['010-12345678']
>>> 
