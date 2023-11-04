import re
import time as t
import requests
from pathlib import Path
import pdfkit

import datetime
list3=[]
list1=[]
list2=[]
import pdfkit
import time
import datetime

for PAGENUM in range(1,2):

    url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=168&PAGENUM=1&urltype=tree.TreeTempUrl&wbtreeid=1010'.format(PAGENUM)

    head = {
             'cookie': 'JSESSIONID=1E33E078980BA363B3077FA8DC1F59E8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        }
    r = requests.get(url,headers=head)
    html_data=r.text
    with open('shuju.txt','w',encoding='utf-8')as f :
         f.write(html_data)
    with open(r"D:\BaiduNetdiskDownload\编程\爬虫\shuju.txt",'r',encoding='utf-8')as f:
         data=f.read()
    res=re.findall('<div\sclass="leftNews3".*?_\d.*?<a\shref="(.*?)"\starget=_blank\stitle=".*?"\ssty.*?/div>',data,re.S)
    res2=re.findall('<div\sclass="leftNews3".*?_\d.*?<a\shref=".*?"\starget=_blank\stitle="(.*?)"\ssty.*?/div>',data,re.S)

    for i in res:
        res1=re.match('http.*?', i, re.S)
        str1=str(res1)
        if str1=='None':
            b='https://www.bkjx.sdu.edu.cn/'
            c=b+i


            list1.append(c)


    for i1 in res2:

        list2.append(i1)
    dict3=dict(zip(list2,list1))
print(type(dict3.keys()))
import pandas as pd

pf=pd.DataFrame(list1)

pf1=pd.DataFrame(list2)
pf2=pd.concat([pf,pf1],axis=1)
pf2.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.3的标题与网站.xlsx',index=False)
print(list1)
i1=1
i2=list2[i1]
for i in list1:
    url=i
    head = {
        'cookie': 'JSESSIONID=1E33E078980BA363B3077FA8DC1F59E8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    r = requests.get(url, headers=head)
    html_data = r.text
    with open('shujuju.txt', 'w', encoding='utf-8')as f:
        f.write(html_data)
    with open(r"D:\BaiduNetdiskDownload\编程\爬虫\shujuju.txt", 'r', encoding='utf-8')as f:
        data = f.read()
    cc = re.sub('[A-Za-z,<,>,=,",仿宋,微软雅黑,/,.,-,:,;,\s,\n]', '', data)
    t.sleep(1)
    print(cc)
    list3.append(cc)

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver =webdriver.Edge()
    driver.get(i)


    driver.maximize_window()
    '''
        根据url，将文章保存到本地
        :param url:
        :return:
        '''
    start = datetime.datetime.now()
    print(start)
    # 本来直接调用pdfkid的from方法就可以了，但是由于我们的wkhtmltopdf安装包有点问题，一直没法搜到，所以只能用本办法，直接配置了wk的地址
    # wkhtmltopdf下载链接： https://wkhtmltopdf.org/downloads.html
    config = pdfkit.configuration(wkhtmltopdf=r'D:\wkpdf\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_url(url, rf"C:\Users\33566\Pictures\Screenshots\%s{i2}.pdf".format(i2) % time.strftime('%Y-%m-%d-%H-%M-%S',
                                                                                       time.localtime(time.time())),
                    configuration=config)
    end = datetime.datetime.now()
    print(end)
    print(end - start)
    i1+=1
    t.sleep(1)
i=['正文']
data = pd.DataFrame(list3,columns=i )
data.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.3正文.xlsx',index=False)