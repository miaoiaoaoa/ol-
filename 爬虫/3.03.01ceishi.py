'''
目前还差一个循环
'''
import requests
for PAGENUM in range(1,20):

    url = 'https://www.bkjx.sdu.edu.cn/sanji_list.jsp?totalpage=168&PAGENUM={}&urltype=tree.TreeTempUrl&wbtreeid=1010'.format(PAGENUM)

    head = {
             'cookie': 'JSESSIONID=1E33E078980BA363B3077FA8DC1F59E8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        }
    r = requests.get(url,headers=head)
    html_data=r.text
    with open('shuju.txt','w',encoding='utf-8')as f :
         f.write(html_data)