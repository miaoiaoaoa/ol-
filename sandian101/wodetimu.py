from operator import itemgetter
import time
import xlwt
from collections import Counter
import openpyxl
import  requests
list0 = []#主数据列表
list1 = []#通过数据列表
list2=[]#题目次数列表
dict0={}
list3=[]
# 或者新建一个工作簿
workbook = openpyxl.Workbook()

# 选择一个工作表
sheet = workbook.active
for pageNow in range(1,201):

    url = 'https://oj.qd.sdu.edu.cn/api/submit/list?pageNow={}&pageSize=20'.format(pageNow)

    head = {
             'cookie': 'UM_distinctid=1837e7ffbf6dda-0360993970b77c-78565470-1fa400-1837e7ffbf7fa1; CNZZDATA1279807957=36991445-1664272379-null%6',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        }
    r = requests.get(url,headers=head)
    data = r.content
    json_data=r.json()

    aa = json_data['data']['rows']

    bb = json_data['data']["pageIndex"]
    print(f'在爬第{bb}页')
    time.sleep(0.2)
    for items in aa:
        keys = ['problemTitle', 'problemCode', 'judgeScore', 'usedTime', 'usedMemory', 'username']
        out = itemgetter(*keys)(items)  # 元组迭代
        out1=list(out)
        list0.append(out1)
        if 1:
            list2.append(items['problemTitle'])
        else:
            continue
        if  items['judgeScore']==100:
            list1 .append(items['problemTitle'])
        else:
            continue
def ton_ji(list):           #数据统计模块
    global set
    set=(list)
    dict={}
    for item in set:
        dict.update({item:list.count(item)})
    collection_words = Counter(list)
    most_counterNum = collection_words.most_common(10)
    print(most_counterNum)
    print(type(most_counterNum))
    return most_counterNum

ton_ji(list2)
ton_ji(list1)
list8=ton_ji(list1)
list9=ton_ji(list2)
import pandas as pd
i=['题目名称','题目ID','分数','时间','内存','用户']
data = pd.DataFrame(list0,columns=i )
data.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.1的题目记录.xlsx',index=False)
i1=['题目名称','次数']
data1=pd.DataFrame(list8,columns=i1)
data1.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.1的AC前十.xlsx',index=False)
i2=['题目名称','次数']
data2=pd.DataFrame(list9,columns=i2)
data2.to_excel(r'D:\BaiduNetdiskDownload\编程\爬虫\3.1的提交前十.xlsx',index=False)
