#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys
from ui import View
from PyQt4 import QtGui


'''
    program: Hary
     author: Hacra
    version: 1.0.1
  startDate: 2017-11-05 night
currentDate: 2017-11-10 night
    address: school(Changchun)
       mail: 2199887379@qq.com
   function: 通过Python爬取ZOL壁纸网站中的壁纸，展示在Pyqt4图形界面之上，并可以设置时间间隔来自动更新壁纸
    explain: 壁纸资源来自ZOL壁纸网站(http://desk.zol.com.cn/)

HHHHHHHHH    HHHHHHHHH
 HHHHHHH      HHHHHHH
  HHHH         HHHH
  HHHH         HHHH
  HHHH         HHHH
  HHHH         HHHH
  HHHH         HHHH            aaaaaa                   ccccc              rrrr      rrr             aaaaaa
  HHHH         HHHH         aaaaaaaaaaaa             ccccccccccc       rrrrrrrr   rrrrrrrr        aaaaaaaaaaaa
  HHHH         HHHH       aaaa       aaaa          ccccc     cccc           rrr rrrr  rrrrr     aaaa       aaaa
  HHHHHHHHHHHHHHHHH       aaaa        aaaa        cccc       ccccc          rrrrrr    rrrr      aaaa        aaaa
  HHHH         HHHH       aaaa        aaaa       ccccc       cccc           rrrrr               aaaa        aaaa
  HHHH         HHHH              aaaaaaaaa       cccc          c            rrrr                       aaaaaaaaa
  HHHH         HHHH          aaaaaaaaaaaaa       cccc                       rrr                    aaaaaaaaaaaaa
  HHHH         HHHH        aaaaa      aaaa       cccc                       rrr                  aaaaa      aaaa
  HHHH         HHHH       aaaa        aaaa       cccc                       rrr                 aaaa        aaaa
  HHHH         HHHH      aaaa         aaaa       cccc            cc         rrr                aaaa         aaaa
  HHHH         HHHH      aaaa         aaaa aa    ccccc          cc          rrr                aaaa         aaaa aa
  HHHH         HHHH      aaaa        aaaaa aa     cccc         ccc          rrr                aaaa        aaaaa aa
  HHHHH        HHHHH      aaaaaaaaaaaaaaaaaaa      cccccccccccccc           rrrr                aaaaaaaaaaaaaaaaaaa
HHHHHHHHH    HHHHHHHHH     aaaaaaaaa   aaaaa         cccccccccc        rrrrrrrrrrrrrr             aaaaaaaa   aaaaa

'''
if __name__ == '__main__':
    path = r'D:/Hary/res/background.jpg'
    app = QtGui.QApplication(sys.argv)
    # 软件窗口
    window = View.Ui_MainWindow()
    palette = QtGui.QPalette()
    palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap(path)))
    window.setPalette(palette)
    # 初始化壁纸
    window.clsWallpaper()
    window.show()
    sys.exit(app.exec_())
