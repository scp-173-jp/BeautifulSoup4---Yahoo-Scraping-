import requests
import pandas as pd
from bs4 import BeautifulSoup
import pdb
from pandas import Series, DataFrame
import codecs

url = 'https://news.yahoo.co.jp/topics/top-picks?page=1'
res = requests.get(url)
title_list = []
date_list = []
link_list = []
for x in range(18):
    x += 1
    url = 'https://news.yahoo.co.jp/topics/top-picks?page=' + str(x)
    res = requests.get(url)
    print(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_title = soup.find_all('div', attrs={'class': 'newsFeed_item_title'})
    news_date = soup.find_all('time', attrs={'class': 'newsFeed_item_date'})
    news_link = soup.find_all('a', attrs={'class': 'newsFeed_item_link'})
    for i in range(25):
        title_res = news_title[i].text
        date_res = news_date[i].text
        link_res = news_link[i].get('href')
        print(title_res)
        print(date_res)
        print(link_res)
        title_list.append(title_res)
        date_list.append(date_res)
        link_list.append(link_res)

print(title_list)
print(date_list)
print(link_list)
df = pd.DataFrame()
df['タイトル'] = title_list
df['日付'] = date_list
df['リンク'] = link_list
df.to_csv('output-result.csv', index=False)
