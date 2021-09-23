#!/bin/python3.8
import requests
import json
from bs4 import BeautifulSoup


# time_type:  Weekly, Monthly , Daily
def crawler( time_type ):

    headers = {
        'authority': 'cn.investing.com',
        'sec-ch-ua': '"Microsoft Edge";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
        'accept': 'text/plain, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded',
        'x-requested-with': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://cn.investing.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://cn.investing.com/equities/apple-computer-inc-historical-data',
        'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,ja;q=0.5',
    }
    
    # 位不同日期型態指定開始時間(時間範圍)
    st_date={'Daily':'2021/08/23' , 'Weekly':'2019/10/05' ,'Monthly':'2019/10/05'}

    data = {
      'curr_id': '6408',
      'smlID': '1159963',
      'header': 'AAPL\u5386\u53F2\u6570\u636E',
      'st_date': st_date[time_type],
      'end_date': '2021/09/23',
      'interval_sec': time_type,
      'sort_col': 'date',
      'sort_ord': 'DESC',
      'action': 'historical_data'
    }

    r = requests.post('https://cn.investing.com/instruments/HistoricalDataAjax', headers=headers, data=data)


    # 確認是否下載成功
    if r.status_code != requests.codes.ok:
        print(r.status_code, " error" )
        exit(1)

    # 以 BeautifulSoup parse HTML text
    soup = BeautifulSoup(r.text, 'html.parser')

    # css selector, get items
    items = soup.select('#curr_table > thead + tbody > tr')

    dictArry=[]

    for item in items:
      item = BeautifulSoup( str(item) ,'html.parser')
      trs = item.find_all( 'td' )
      dic={}
      dic['日期']=trs[0].text
      dic['收盘']= trs[1].text
      dic['开盘']= trs[2].text
      dic['高']= trs[3].text
      dic['低']= trs[4].text
      dic['交易量']= trs[5].text
      dic['涨跌幅']=trs[6].text
      dictArry.append(dic)
      
    json_object = json.dumps( dictArry,indent=4,ensure_ascii=False)
    return json_object



# 指定三種之一 time_type
# time_type:  Weekly, Monthly , Daily

# print( crawler('Weekly') )
# print( crawler('Monthly') )
print( crawler('Daily') )

