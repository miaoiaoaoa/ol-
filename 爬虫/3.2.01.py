

# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup

# 初始化Session对象，利用session维持一个会话
session = requests.Session()

# 设置请求表头
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

# 设置请求的URL
url_login = 'https://oj.qd.sdu.edu.cn/api/contest/query?contestId=286'

# 设置请求表单
form_data = {
'redir': '',
'form_email': '账号',
'form_password': '密码',
'login': u'登陆'
}

# 用Session对象的post()方法模拟登录
response = session.post(url_login, data=form_data, headers=headers)



