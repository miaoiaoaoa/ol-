
# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:ZSW
@file:htmltopdf.py
@time:2020/09/14
"""
import pdfkit
import time
import datetime
def save_to_pdf(url):
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
    pdfkit.from_url(url, r"C:\Users\33566\Pictures\Screenshots\%s.pdf"%time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())), configuration=config)
    end = datetime.datetime.now()
    print(end)
    print(end - start)

if __name__ =='__main__':
    url = "https://www.sohu.com/"
    save_to_pdf(url)




