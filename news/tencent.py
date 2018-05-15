#!/usr/bin/env python
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json

from news.news_object import News


def get_news_from_tencent(site_url):
    result = []
    # url = ''
    res = requests.get(site_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    q_tpList = soup.select('.Q-tpList')
    # print(q_tpList.__sizeof__())
    # print(q_tpList)
    count = q_tpList.__sizeof__()
    print(count)
    for i in range(count):
        q_tpWrap = ''
        try:
            # 这里报错说明爬取规则变化了,结束爬取
            q_tpWrap = q_tpList[i].select('.Q-tpWrap')[0]
        except IndexError:
            break

        news_pic_url = ''
        try:
            news_pic_url = q_tpWrap.select('.pic')[0].select('img')[0]['src']
        except KeyError:
            # print('-----------------------------------------------------------')
            # print(":::::::", q_tpWrap)
            news_pic_url = q_tpWrap.select('.pic')[0].select('img')[0]['_src']
            # print('-----------------------------------------------------------')
        try:
            news_title = q_tpWrap.select('.linkto')[0].text  # 新闻标题
        except IndexError:
            # print('-----------------------------------------------------------')
            # print(":::::::", q_tpWrap)
            # print('-----------------------------------------------------------')
            news_title = str(q_tpWrap.select('p')[0].contents[0]).strip()  # 新闻标题
        try:
            news_detail_url = q_tpWrap.select('.linkto')[0]['href']  # 新闻详细内容地址
        except IndexError:
            # print('-----------------------------------------------------------')
            # print(":::::::", q_tpWrap)
            # print('-----------------------------------------------------------')
            news_detail_url = q_tpWrap.select('.pic')[0]['href']  # 新闻详细内容地址
        # result[i] = json.dumps(News(title=news_title, content=news_detail_url, pic_url=news_pic_url))
        item = {"title": news_title, "content": news_detail_url, "picUrl":news_pic_url}
        result.append(item)
    # return json.dumps(result)
    return result


if __name__ == '__main__':
    site_url = "http://news.qq.com/"
    get_news_from_tencent(site_url)
