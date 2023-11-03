from operator import itemgetter

import requests
import xlwt
import openpyxl
list = []

# 或者新建一个工作簿
workbook = openpyxl.Workbook()

# 选择一个工作表
sheet = workbook.active
for pageNow in range(1,6):

    url = 'https://oj.qd.sdu.edu.cn/api/problem/list?pageNow={}&pageSize=20'.format(pageNow)

    head = {
        'cookie': 'UM_distinctid=1837e7ffbf6dda-0360993970b77c-78565470-1fa400-1837e7ffbf7fa1; CNZZDATA1279807957=36991445-1664272379-null%6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
    r = requests.get(url, headers=head)
    data = r.content
    json_data = r.json()
    aa = json_data['data']['rows']
    for items in aa:
        keys = ['problemId', 'problemCode', 'problemTitle', 'submitNum', 'acceptNum']
        out = itemgetter(*keys)(items)  # 元组迭代
        list.append(out)

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'sheet'
    ws.append(('编号', '题号', '题目', '测试数', '通过数'))
    for row in list:
        ws.append(row)
    wb.save("D:\BaiduNetdiskDownload\编程\爬虫\公开题目.xlsx")
