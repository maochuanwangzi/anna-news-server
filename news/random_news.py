#!/usr/bin/env python
# coding=utf-8
"""
所有新闻的json 包括title content pic_url news_detail_url
"""
# python manage.py runserver 0.0.0.0:8001
# ln -s /usr/anaconda3/bin/python3 /usr/bin/python3.6
import json
from django.http import HttpResponse
from django.shortcuts import render
import requests

from news.netease import get_news_from_netease
from news.sohu import get_news_from_sohu
from news.tencent import get_news_from_tencent

tencent_news_url = 'http://news.qq.com/'
netease_news_url = 'http://news.163.com/'
sohu_news_url = 'http://news.sohu.com/'
site_name_url_dic = {"tencent":tencent_news_url, "netease":netease_news_url, "sohu":sohu_news_url}

def get_news_by_site_name(request, site_name):
    try:
        site_url = site_name_url_dic[site_name]
    except KeyError as e:
        content = {'API ERRO': str(e)}
        # print(content)
        # return content
    # print(site_name)
    # print(site_url)
    if site_name == "tencent":
        content = get_news_from_tencent(site_url)
    elif site_name == 'netease':
        content = get_news_from_netease(site_url)
    elif site_name == 'sohu':
        content = get_news_from_sohu(site_url)

    return HttpResponse(json.dumps(content), content_type="application/json")



