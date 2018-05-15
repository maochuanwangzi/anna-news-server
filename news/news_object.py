#!/usr/bin/env python
# coding=utf-8

class News:
    title =''
    content = ''
    pic_url = ''
    # news_date = ''
    # comments_number=0
    # comments_list = {}

    def __init__(self, title, content, pic_url):
        self.title = title
        self.content = content
        self.pic_url = pic_url
        # self.news_date = news_date
        # self.comments_number = comments_number
        # self.comments_list = comments_list