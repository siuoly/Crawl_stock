# Crawl_stock



## Prerequisite

```
pip install beautifulsoup4
pip install requests
pip install json5
```



### Usage

```
python3.8 crawl.py
```

function `crawler('Daily')` ,`crawler('Monthly')`, and `crawler('Weekly')` return corresponding json object.

### Method:

一開始直接爬取網頁資料"https://cn.investing.com/equities/apple-computer-inc-historical-data"，但是bs4無法取得dropdown list的response.換一個方法。

在chrome開發者工具，找出"HistoricalDataAjax"為網頁請求的資料檔。為了重現chrome執行的request請求，在此複製cURL命令

![](https://i.imgur.com/LZLfDKo.png)


到[curl.trillworks](https://curl.trillworks.com/)轉換`curl command`為實際呼叫的python code。

![](https://i.imgur.com/tXkfOSk.png)


接著修改對應的日期請求格式。工作完成。

![](https://i.imgur.com/UpjMQw2.png)
