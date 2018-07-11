#!/usr/bin/env python
# -*- coding:utf-8 -*-


import win32api
import win32con
import win32gui
import requests
from PIL import Image
from io import BytesIO
from util import ZolUrl


# 设置桌面壁纸
# url: 壁纸链接
# dim: 壁纸尺寸
def setWallpaper(url, dim):
    # 壁纸路径
    path = r'D:\Hary\wallpaper\wallpaper.bmp'
    # 如果壁纸下载成功，则设置桌面壁纸，并返回True
    if downloadWallpaper(url, dim, path):
        try:
            reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
            win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")
            win32api.RegSetValueEx(reg_key, "TileWallpaper", 0, win32con.REG_SZ, "0")
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
            return True
        except Exception as e:
            print('<Wallpaper.py>', e)
            return False
    # 或者返回False
    else:
        return False


# 下载壁纸
# url: 壁纸链接
# dim: 壁纸尺寸
# path: 壁纸路径
def downloadWallpaper(url, dim, path):
    # 获取壁纸大图链接
    img_url = ZolUrl.getBigWallpaperUrl(url, dim)
    # 如果获取失败，则返回False
    if img_url is None:
        return False
    # 下载壁纸，并返回True
    img = Image.open(BytesIO(requests.get(img_url).content))
    img.save(path, 'BMP')
    return True
