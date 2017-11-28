'''
这个程序实现的功能是抓取晋江文学城前100页的作者、作品名及作品链接。
'''
#导入相应的模块
import urllib.request
import re

#定义几个列表，用于存放爬取到的东西。
zhuozhe = []
shuming = []
lianjie = []
lianjie2 = []

#使用正则爬取作者、作品名及链接。
for i in range(0,101):
    if i == 1:
        continue
    url = "http://www.jjwxc.net/bookbase_slave.php?page="+str(i)
    data = urllib.request.urlopen(url).read().decode("gbk","ignore")
    pat0 = ''''#eefaee';">.*?target="_blank">(.*?)<'''     #作者
    pat1 = '" class="tooltip">(.*?)<'       #作品名
    pat2 = '<td align="left"><a href="(.*?)" target="_blank" rel="'
    rst0 = re.compile(pat0,re.S).findall(data)
    rst1 = re.compile(pat1).findall(data)
    rst2 = re.compile(pat2).findall(data)
    for j in range(0,len(rst2)):
        zhuozhe.append(rst0[j])
        shuming.append(rst1[j])
        lianjie.append(rst2[j])
for i in range(0,len(lianjie)):
    url = "http://www.jjwxc.net/" + lianjie[i]
    lianjie2.append(url)

#将爬取到的东西存放到本地文件中。
fh = open("D:/test1/jinjian.txt","w")
fh.write("作者 --- 作品名 --- 作品链接\n\n")
for j in range(0,len(zhuozhe)):
    fh.write(str(zhuozhe[j])+" --- "+str(shuming[j])+" --- "+str(lianjie2[j])+"\n\n")
fh.close()
