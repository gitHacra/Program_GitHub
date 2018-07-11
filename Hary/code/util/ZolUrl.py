#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re
import requests


# 获取20张壁纸链接
# cls: 壁纸分类
# dim: 壁纸尺寸
# index: 网页下标
def getAllWallpaperUrl(cls, dim, index):
    zol_url_s = []      # 小图壁纸链接列表
    zol_url_h = []      # 大图网页链接列表
    # 如果壁纸不足20张，则继续获取
    while len(zol_url_s) < 20:
        try:
            # ZOL壁纸网站链接
            zol_url = 'http://desk.zol.com.cn/' + cls + '/' + dim + '/' + str(index) + '.html'
            # 网页源码
            html = requests.get(zol_url, timeout=2)
            html.encoding = 'GB2312'
            text = html.text
            text = text[text.find('pic-list2  clearfix">'):text.find('分页')]
            # 大图网页链接列表
            rg = 'href="([\w\W]+?)"'
            zol_url_h += re.findall(rg, text)
            # 小图壁纸链接列表
            rg = 'src="([\w\W]+?)"'
            zol_url_s += re.findall(rg, text)
            # 如果当前为最后一页，则爬取第一张
            if len(zol_url_s) < 15:
                index = 0
            # 或者爬取下一页
            else:
                index += 1
        except Exception as e:
            print('<ZolUrl.py - getAllImgUrl>', e)
            return [], []
    return zol_url_s, zol_url_h


# 获取壁纸大图链接
# url: 大图网页链接
# dim: 壁纸尺寸
def getBigWallpaperUrl(url, dim):
    try:
        # 获取网页源码
        url = 'http://desk.zol.com.cn' + url
        text = requests.get(url, timeout=2).text
        rg = dim + '" href="([\w\W]+?)"'
        url = 'http://desk.zol.com.cn' + re.findall(rg, text)[0]
        text = requests.get(url, timeout=2).text
        # 返回壁纸链接
        rg = 'img src="([\w\W]+?)"'
        return re.findall(rg, text)[0]
    except Exception as e:
        print('<ZolUrl.py - getBigImgUrl>', e)
        return None
