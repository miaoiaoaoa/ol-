import requests
import time as t
import json
from operator import itemgetter
import ssl
list1=[]
list2=[]
list3=[]
ssl._create_default_https_context = ssl._create_unverified_context
requests.packages.urllib3.disable_warnings
session = requests.session()
url = 'https://oj.qd.sdu.edu.cn/api/contest/query?contestId=286'
proxies={'http':'http://127.0.0.1:8080'}
data={"username":"OL2023u008","password":"OL2023u008"}
login_page ='https://oj.qd.sdu.edu.cn/api/user/login'


headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/json;charset=UTF-8'
    }


res2=session.post(login_page,data=json.dumps(data),headers=headers,proxies=proxies,verify=0)
print(res2.content)
res1=session.get(url,headers=headers) #这种是登录前和登录后url不同的情况
print((res1.content))
json_data=res1.json()
aa=json_data['data']['problems']
print(aa)
for items in aa:
    keys = ['problemTitle', 'problemCode', 'acceptNum', 'submitNum', 'judgeResult', 'judgeScore']
    out = itemgetter(*keys)(items)  # 元组迭

    out1=list(out)

    list1.append(out1)
    if out[5]!=100:
        list2.append(out1[0])
        list3.append(out1[4])
print(list2)
import pandas as pd
i=['题目名称','题目ID','通过数','提交数','我的结果','我的分数']
data = pd.DataFrame(list1,columns=i )
data.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.2我的记录.xlsx',index=False)
i1=['我还没有AC的题目']
data = pd.DataFrame(list2,columns=i1)
data.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.2我的AC记录.xlsx',index=False)
from plotly.graph_objects import Pie, Figure, layout
from plotly.colors import qualitative

# 用于绘图的源数据
industry = list2
number=list3

# 初始化一个空白图表
fig_donut = Figure()

# 创建环形图形式的数据图形
trace_donut = Pie(labels=industry,
                  values=number,
                  hole=0.5,
                  pull=[0.1],
                  textinfo='label+percent',
                  marker_colors=qualitative.Pastel)

# 将数据图形添加到图表中
fig_donut.add_trace(trace_donut)

# 调整图表布局
fig_donut.update_layout(paper_bgcolor='rgb(229,249,229)',
                        title=layout.Title(text='我的提交'))

# 展示生成的图表
fig_donut.show()