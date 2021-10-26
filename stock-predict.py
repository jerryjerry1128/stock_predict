# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:23:59 2021

@author: User
"""
from selenium import webdriver # 匯入 selenium 的 webdriver
from time import sleep         # 匯入內建 time 模組的 sleep() 函式
from datetime import date
import requests  # 匯入 requests 套件
from bs4 import BeautifulSoup
while True:
    html = requests.get('https://www.twse.com.tw/zh/listed/listingProfileInquiry?mobile=&selectItem=2&selectSubitem=3') 
    bs = BeautifulSoup(html.text, 'lxml')
    stock = bs.find_all('td')
    stock_code=[]
    stock_name=[]
    stock_now=[]
    stock_pre=[]
    stock_ratio=[]
    for i in range(len(stock)):
        if (i+1)%5==1:
            stock_code.append(stock[i].text.strip())
        elif (i+1)%5==2:
            stock_name.append(stock[i].text.strip())
        elif (i+1)%5==3:
            stock_now.append(stock[i].text.strip())
        elif (i+1)%5==4:
            stock_pre.append(stock[i].text.strip())
        else:
            stock_ratio.append(float(stock[i].text.strip()))
    
    
    browser = webdriver.Chrome()            # 建立 Chrome 瀏覽器物件
    
    
    for i in range(5):
        if stock_ratio[i]>=2:
            print('股票代號:'+stock_code[i]+' 股票名稱:'+stock_name[i]+' 當日成交量: '+stock_now[i]+' 昨日成交量:'+stock_pre[i]+' 倍率:'+str(stock_ratio[i])+'\n')
            browser.get('https://s.yimg.com/nb/tw_stock_frontend/scripts/StxChart/StxChart.9d11dfe155.html?sid='+stock_code[i])
            browser.set_window_rect(200, 100, 650, 520)
            #sleep(3) # 暫停 3 秒
            browser.save_screenshot(str(date.today())+'_'+stock_code[i]+'.png')
            sleep(1)
    
    print('各股票分析圖請至資料夾與執行檔同層尋找\n')
    print('若委買賣差>0 或 委買賣比>1，則代表買入量>賣出量')
    browser.quit()
    stop=input('輸入s可以結束此程式: ')
    if stop.lower() == 's':
        break