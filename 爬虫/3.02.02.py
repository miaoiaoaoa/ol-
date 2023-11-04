import requests
from operator import itemgetter
import time as t
import json
import ssl
list1=[]
for pageNow in range(1,3):
    ssl._create_default_https_context = ssl._create_unverified_context
    requests.packages.urllib3.disable_warnings
    session = requests.session()

    url = 'https://oj.qd.sdu.edu.cn/api/contest/listSubmission?pageNow={}&pageSize=20&contestId=286'.format(pageNow)

    proxies={'http':'http://127.0.0.1:8080'}
    data={"username":"OL2023u008","password":"OL2023u008"}
    login_page ='https://oj.qd.sdu.edu.cn/api/user/login'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/json;charset=UTF-8'
        }

    t.sleep(1)
    res2=session.post(login_page,data=json.dumps(data),headers=headers,proxies=proxies,verify=0)
    print(res2.content)
    res1=session.get(url,headers=headers) #这种是登录前和登录后url不同的情况
    data1= res1.json()
    data2=res2.json()
    aa=data1['data']['rows']
    print(aa)
    for items in aa:
        keys = ['problemTitle', 'problemCode', 'judgeScore', 'usedTime', 'usedMemory', 'username']
        out = itemgetter(*keys)(items)  # 元组迭代
        out1=list(out)
        list1.append(out1)
        print(list1)
import pandas as pd
i=['题目名称','题目ID','分数','时间','内存','用户']
data = pd.DataFrame(list1,columns=i )
data.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.2题目记录.xlsx',index=False)

