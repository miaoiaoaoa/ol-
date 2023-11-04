from bs4 import BeautifulSoup
import requests
url = 'https://oj.qd.sdu.edu.cn/api/problem/list?pageNow=1&pageSize=20'

head = {
        'cookie': 'UM_distinctid=1837e7ffbf6dda-0360993970b77c-78565470-1fa400-1837e7ffbf7fa1; CNZZDATA1279807957=36991445-1664272379-null%6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    }
r = requests.get(url, headers=head)
data = r.content
s =BeautifulSoup(data,"html.pasrer")
