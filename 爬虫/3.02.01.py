from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time as t

# 设置Chrome驱动程序路径
driver = webdriver.Chrome(r"C:\Users\33566\Desktop\Google Chrome.lnk")

# 打开网页
driver.get('https://www.bkjx.sdu.edu.cn/sanji_list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010')

# 找到要点击的按钮元素
button = driver.find_element(By.XPATH, '//button[@id=""<a href="content.jsp?urltype=news.NewsContentUrl&wbtreeid=1266&wbnewsid=36794" target="_blank" title="关于评选2023年度山东大学大学生创新创业教育先进集体、先进工作者和优秀指导教师的通知" style>关于评选2023年度山东大学大学生创新创业教育先进集体、先进工作者和优秀指导教师...</a>]')

# 模拟点击按钮
button.click()
t.sleep(5)
# 关闭浏览器
driver.quit()
