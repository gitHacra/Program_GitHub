# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Program_python\Hary\ui\Hary.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


import time
import random
import requests
import threading
from util import ZolUrl, Wallpaper
from PyQt4 import QtCore, QtGui, QtWebKit


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    __index = 0                             # 壁纸更换下标
    __index2 = 0                            # 查看大图下标
    __path = r'D:\Hary\res\hary.jpg'        # 默认图片路径
    __status = '全部(1920x1080)'             # 状态栏的内容
    __img_url_s = []                        # 小图链接列表
    __img_url_h = []                        # 大图链接列表
    __di = ['all', 'fengjing', 'dongman', 'meinv', 'chuangyi', 'katong', 'youxi', 'keai', 'mingxing',
            'jianzhu', 'zhiwu', 'dongwu', 'yingshi', 'xingzuo', 'meishi', 'jieri', 'qiche', 'jingwu',
            'chemo', 'tiyu', 'pinpai', 'qita']                  # 壁纸分类列表
    __si = ['1920x1080', '1680x1050', '1440x900', '1366x768']   # 壁纸尺寸列表
    __ti = [0, 300, 600, 1200, 1800]                            # 更新间隔列表

    # 初始化
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)          # 初始化界面
        self.retranslateUi(self)    # 初始化界面
        self.alterUi()              # 更改界面
        self.onClick()              # 控件事件监听

    # 初始化界面
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.setMinimumSize(QtCore.QSize(1140, 680))
        MainWindow.setMaximumSize(QtCore.QSize(1140, 680))
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_1 = QtGui.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(37, 17, 80, 20))
        self.label_1.setObjectName(_fromUtf8("label_1"))
        self.comboBox_1 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_1.setGeometry(QtCore.QRect(122, 14, 65, 26))
        self.comboBox_1.setObjectName(_fromUtf8("comboBox_1"))
        self.comboBox_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.comboBox_1.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(214, 17, 80, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox_2 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(299, 13, 200, 28))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(641, 17, 80, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBox_4 = QtGui.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(726, 14, 80, 26))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.pushButton_1 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(836, 13, 65, 28))
        self.pushButton_1.setObjectName(_fromUtf8("pushButton_1"))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.line_1 = QtGui.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(0, 54, 1150, 5))
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 70, 1079, 546))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayoutWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gridLayoutWidget.setToolTip('单击查看大图')
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.webView_01 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_01.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_01.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_01.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_01.setObjectName(_fromUtf8("webView_01"))
        self.gridLayout.addWidget(self.webView_01, 1, 0, 1, 1)
        self.webView_02 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_02.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_02.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_02.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_02.setObjectName(_fromUtf8("webView_02"))
        self.gridLayout.addWidget(self.webView_02, 1, 1, 1, 1)
        self.webView_03 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_03.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_03.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_03.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_03.setObjectName(_fromUtf8("webView_03"))
        self.gridLayout.addWidget(self.webView_03, 1, 2, 1, 1)
        self.webView_04 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_04.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_04.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_04.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_04.setObjectName(_fromUtf8("webView_04"))
        self.gridLayout.addWidget(self.webView_04, 1, 3, 1, 1)
        self.webView_05 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_05.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_05.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_05.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_05.setObjectName(_fromUtf8("webView_05"))
        self.gridLayout.addWidget(self.webView_05, 1, 4, 1, 1)
        self.webView_06 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_06.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_06.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_06.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_06.setObjectName(_fromUtf8("webView_06"))
        self.gridLayout.addWidget(self.webView_06, 2, 0, 1, 1)
        self.webView_07 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_07.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_07.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_07.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_07.setObjectName(_fromUtf8("webView_07"))
        self.gridLayout.addWidget(self.webView_07, 2, 1, 1, 1)
        self.webView_08 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_08.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_08.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_08.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_08.setObjectName(_fromUtf8("webView_08"))
        self.gridLayout.addWidget(self.webView_08, 2, 2, 1, 1)
        self.webView_09 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_09.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_09.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_09.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_09.setObjectName(_fromUtf8("webView_09"))
        self.gridLayout.addWidget(self.webView_09, 2, 3, 1, 1)
        self.webView_10 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_10.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_10.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_10.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_10.setObjectName(_fromUtf8("webView_10"))
        self.gridLayout.addWidget(self.webView_10, 2, 4, 1, 1)
        self.webView_11 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_11.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_11.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_11.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_11.setObjectName(_fromUtf8("webView_11"))
        self.gridLayout.addWidget(self.webView_11, 3, 0, 1, 1)
        self.webView_12 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_12.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_12.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_12.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_12.setObjectName(_fromUtf8("webView_12"))
        self.gridLayout.addWidget(self.webView_12, 3, 1, 1, 1)
        self.webView_13 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_13.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_13.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_13.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_13.setObjectName(_fromUtf8("webView_13"))
        self.gridLayout.addWidget(self.webView_13, 3, 2, 1, 1)
        self.webView_14 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_14.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_14.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_14.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_14.setObjectName(_fromUtf8("webView_14"))
        self.gridLayout.addWidget(self.webView_14, 3, 3, 1, 1)
        self.webView_15 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_15.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_15.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_15.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_15.setObjectName(_fromUtf8("webView_15"))
        self.gridLayout.addWidget(self.webView_15, 3, 4, 1, 1)
        self.webView_16 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_16.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_16.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_16.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_16.setObjectName(_fromUtf8("webView_16"))
        self.gridLayout.addWidget(self.webView_16, 4, 0, 1, 1)
        self.webView_17 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_17.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_17.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_17.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_17.setObjectName(_fromUtf8("webView_17"))
        self.gridLayout.addWidget(self.webView_17, 4, 1, 1, 1)
        self.webView_18 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_18.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_18.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_18.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_18.setObjectName(_fromUtf8("webView_18"))
        self.gridLayout.addWidget(self.webView_18, 4, 2, 1, 1)
        self.webView_19 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_19.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_19.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_19.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_19.setObjectName(_fromUtf8("webView_19"))
        self.gridLayout.addWidget(self.webView_19, 4, 3, 1, 1)
        self.webView_20 = QtWebKit.QWebView(self.gridLayoutWidget)
        self.webView_20.setMinimumSize(QtCore.QSize(208, 130))
        self.webView_20.setMaximumSize(QtCore.QSize(208, 130))
        self.webView_20.setUrl(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__path)))
        self.webView_20.setObjectName(_fromUtf8("webView_20"))
        self.gridLayout.addWidget(self.webView_20, 4, 4, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1036, 13, 65, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 初始化界面
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Hary", None))
        self.label_1.setText(_translate("MainWindow", "壁纸分类：", None))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "全部", None))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "风景", None))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "动漫", None))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "美女", None))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "创意", None))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "卡通", None))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "游戏", None))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "可爱", None))
        self.comboBox_1.setItemText(8, _translate("MainWindow", "明星", None))
        self.comboBox_1.setItemText(9, _translate("MainWindow", "建筑", None))
        self.comboBox_1.setItemText(10, _translate("MainWindow", "植物", None))
        self.comboBox_1.setItemText(11, _translate("MainWindow", "动物", None))
        self.comboBox_1.setItemText(12, _translate("MainWindow", "影视", None))
        self.comboBox_1.setItemText(13, _translate("MainWindow", "星座", None))
        self.comboBox_1.setItemText(14, _translate("MainWindow", "美食", None))
        self.comboBox_1.setItemText(15, _translate("MainWindow", "节日", None))
        self.comboBox_1.setItemText(16, _translate("MainWindow", "汽车", None))
        self.comboBox_1.setItemText(17, _translate("MainWindow", "静物", None))
        self.comboBox_1.setItemText(18, _translate("MainWindow", "车模", None))
        self.comboBox_1.setItemText(19, _translate("MainWindow", "体育", None))
        self.comboBox_1.setItemText(20, _translate("MainWindow", "品牌", None))
        self.comboBox_1.setItemText(21, _translate("MainWindow", "其他", None))
        self.label_2.setText(_translate("MainWindow", "壁纸尺寸：", None))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1920x1080(15-23英寸)", None))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1680x1050(22英寸)", None))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1440x900(15-19英寸)", None))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1366x768(14-15英寸)", None))
        self.label_4.setText(_translate("MainWindow", "更新间隔：", None))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "0分钟", None))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "5分钟", None))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "10分钟", None))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "20分钟", None))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "30分钟", None))
        self.pushButton_1.setText(_translate("MainWindow", "更新", None))
        self.pushButton_2.setText(_translate("MainWindow", "随机", None))

    # 退出到系统托盘
    def closeEvent(self, event):
        self.hide()
        self.trayIcon.show()
        event.ignore()

    # 更改界面
    def alterUi(self):
        # 添加软件图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r'D:\Hary\res\icon.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        # 添加系统托盘
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setIcon(QtGui.QIcon(r'D:\Hary\res\icon.ico'))
        self.trayIcon.setToolTip('Hary')
        self.trayIcon.show()
        self.createTrayMenu()
        # 设置默认更新间隔
        self.comboBox_4.setCurrentIndex(3)
        # 设置状态栏背景和高度
        self.statusbar.setStyleSheet('''background-color:#E5E9E8; height:28px''')
        # 添加大图查看控件
        self.bigImg = QtGui.QLabel(self.centralwidget)
        self.bigImg.setGeometry(QtCore.QRect(30, 70, 1079, 556))
        self.bigImg.setObjectName(_fromUtf8("bigImg"))
        self.bigImg.setVisible(False)
        # 添加上一图控件
        self.leftImg = QtGui.QLabel(self.centralwidget)
        self.leftImg.setGeometry(QtCore.QRect(30, 70, 208, 556))
        self.leftImg.setObjectName(_fromUtf8("leftImg"))
        self.leftImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftImg.setPixmap(QtGui.QPixmap(r'D:\Hary\res\left.png'))
        self.leftImg.setToolTip('上一图')
        self.leftImg.setVisible(False)
        # 添加下一图控件
        self.rightImg = QtGui.QLabel(self.centralwidget)
        self.rightImg.setGeometry(QtCore.QRect(901, 70, 208, 556))
        self.rightImg.setObjectName(_fromUtf8("rightImg"))
        self.rightImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rightImg.setPixmap(QtGui.QPixmap(r'D:\Hary\res\right.png'))
        self.rightImg.setToolTip('下一图')
        self.rightImg.setVisible(False)
        # 添加返回主页控件
        self.backImg = QtGui.QLabel(self.centralwidget)
        self.backImg.setGeometry(QtCore.QRect(240, 70, 658, 278))
        self.backImg.setObjectName(_fromUtf8("backImg"))
        self.backImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backImg.setToolTip('返回主页')
        self.backImg.setVisible(False)
        # 添加设为壁纸控件
        self.wallImg = QtGui.QLabel(self.centralwidget)
        self.wallImg.setGeometry(QtCore.QRect(240, 348, 658, 278))
        self.wallImg.setObjectName(_fromUtf8("wallImg"))
        self.wallImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.wallImg.setToolTip('设为壁纸')
        self.wallImg.setVisible(False)
        # 设置webView不可点击
        self.webView_01.setEnabled(False)
        self.webView_02.setEnabled(False)
        self.webView_03.setEnabled(False)
        self.webView_04.setEnabled(False)
        self.webView_05.setEnabled(False)
        self.webView_06.setEnabled(False)
        self.webView_07.setEnabled(False)
        self.webView_08.setEnabled(False)
        self.webView_09.setEnabled(False)
        self.webView_10.setEnabled(False)
        self.webView_11.setEnabled(False)
        self.webView_12.setEnabled(False)
        self.webView_13.setEnabled(False)
        self.webView_14.setEnabled(False)
        self.webView_15.setEnabled(False)
        self.webView_16.setEnabled(False)
        self.webView_17.setEnabled(False)
        self.webView_18.setEnabled(False)
        self.webView_19.setEnabled(False)
        self.webView_20.setEnabled(False)

    # 控件监听
    def onClick(self):
        self.comboBox_1.currentIndexChanged.connect(self.clsWallpaper)    # 壁纸分类更改监听
        self.comboBox_2.currentIndexChanged.connect(self.clsWallpaper)    # 壁纸尺寸更改监听
        self.pushButton_1.clicked.connect(self.updateWallpaper)              # 更新按钮点击监听
        self.pushButton_2.clicked.connect(self.randomWallpaper)           # 随机按钮点击监听

    # 单击查看大图监听
    def mousePressEvent(self, event):
        # 获取点击坐标
        loc = [(event.y() - 80) // 140, (event.x() - 30) // 218]
        if loc[0] < 0 or loc[0] > 3:
            return
        if loc[1] < 0 or loc[1] > 4:
            return
        # 如果处于大图显示界面
        if self.bigImg.isVisible():
            # 如果点击位置处于顶部，则返回主页面
            if 0 <= loc[0] <= 1 and 0 < loc[1] < 4:
                self.bigImg.setVisible(False)
                self.leftImg.setVisible(False)
                self.rightImg.setVisible(False)
                self.backImg.setVisible(False)
                self.wallImg.setVisible(False)
                return
            # 或者点击位置处于底部，则设置为壁纸，并将查看大图下标加一后赋值给壁纸更换下标
            elif 2 <= loc[0] <= 3 and 0 < loc[1] < 4:
                if not Wallpaper.setWallpaper(Ui_MainWindow.__img_url_h[Ui_MainWindow.__index2], Ui_MainWindow.__si[self.comboBox_2.currentIndex()]):
                    self.setStatus('无法联网或壁纸已损坏')
                self.pushButton_1.setText(_translate("MainWindow", "更新", None))
                self.setWindowTitle(_translate("MainWindow", "Hary", None))
                self.trayIcon.setToolTip('Hary')
                Ui_MainWindow.__index = Ui_MainWindow.__index2 + 1
                return
            # 或者点击位置处于左侧，则查看大图下标减一
            elif loc[1] == 0:
                Ui_MainWindow.__index2 = (Ui_MainWindow.__index2 - 1) % 20
            # 或者点击位置处于右侧，则查看大图下标加一
            elif loc[1] == 4:
                Ui_MainWindow.__index2 = (Ui_MainWindow.__index2 + 1) % 20
        # 或着当前处于主页面
        else:
            # 查看大图下标为点击位置坐标
            Ui_MainWindow.__index2 = loc[0] * 5 + loc[1]
        # 由查看大图下标获取大图链接
        img_url = ZolUrl.getBigWallpaperUrl(Ui_MainWindow.__img_url_h[Ui_MainWindow.__index2], Ui_MainWindow.__si[self.comboBox_2.currentIndex()])
        # 如果链接不存在，则更改提示信息
        if img_url is None:
            self.pushButton_1.setText(_translate("MainWindow", "更新", None))
            self.setWindowTitle(_translate("MainWindow", "Hary", None))
            self.trayIcon.setToolTip('Hary')
            self.setStatus('无法联网或壁纸已损坏')
        # 或者链接获取正常，则显示大图查看控件
        else:
            img = QtGui.QPixmap()
            img.loadFromData(requests.get(img_url).content)
            self.bigImg.setPixmap(img.scaled(1079, 556))
            self.wallImg.setVisible(True)
            self.bigImg.setVisible(True)
            self.leftImg.setVisible(True)
            self.rightImg.setVisible(True)
            self.backImg.setVisible(True)

    # 设置状态栏信息
    def setStatus(self, message):
        self.statusBar().showMessage(message)

    # 更新桌面壁纸
    def updateWallpaper(self):
        # 按间隔时间更新壁纸
        def cyc():
            # 间隔时间
            ti = Ui_MainWindow.__ti[self.comboBox_4.currentIndex()]
            while True:
                # 如果成功更新壁纸，则睡眠一个间隔时间
                if Wallpaper.setWallpaper(Ui_MainWindow.__img_url_h[Ui_MainWindow.__index], Ui_MainWindow.__si[self.comboBox_2.currentIndex()]):
                    temp = ti
                    while temp > 0:
                        temp -= 1
                        time.sleep(1)
                        # 如果停止更新后，则结束此循环，并结束此进程
                        if self.pushButton_1.text() == "更新":
                            return
                Ui_MainWindow.__index = (Ui_MainWindow.__index + 1) % 20
        # 如果处于大图显示界面
        if self.bigImg.isVisible():
            # 如果当前不处于更新状态，则直接更新壁纸，并返回主界面
            if self.pushButton_1.text() == '更新':
                if Wallpaper.setWallpaper(Ui_MainWindow.__img_url_h[Ui_MainWindow.__index2],
                                          Ui_MainWindow.__si[self.comboBox_2.currentIndex()]):
                    Ui_MainWindow.__index = Ui_MainWindow.__index2 + 1
                    if self.comboBox_4.currentIndex() >= 0:
                        self.pushButton_1.setText(_translate("MainWindow", "停止", None))
                        self.setWindowTitle(_translate("MainWindow", "Hary - 正在自动更新壁纸", None))
                        self.trayIcon.setToolTip('Hary - 正在自动更新壁纸')
                else:
                    self.setStatus('无法联网或壁纸已损坏')
                self.bigImg.setVisible(False)
                self.leftImg.setVisible(False)
                self.rightImg.setVisible(False)
                self.backImg.setVisible(False)
                self.wallImg.setVisible(False)
            # 或者当前处于更新状态，则关闭更新状态
            else:
                self.pushButton_1.setText(_translate("MainWindow", "更新", None))
                self.setWindowTitle(_translate("MainWindow", "Hary", None))
                self.trayIcon.setToolTip('Hary')
        # 或者当前处于主界面
        else:
            # 如果当前不处于更新状态
            if self.pushButton_1.text() == "更新":
                # 如果当前更新间隔为0，则直接更新壁纸
                if Ui_MainWindow.__ti[self.comboBox_4.currentIndex()] == 0:
                    u = Ui_MainWindow.__img_url_h[Ui_MainWindow.__index]
                    s = Ui_MainWindow.__si[self.comboBox_2.currentIndex()]
                    Ui_MainWindow.__index = (Ui_MainWindow.__index + 1) % 20
                    # 如果更新壁纸失败，则显示提示信息
                    if not Wallpaper.setWallpaper(u, s):
                        self.pushButton_1.setText(_translate("MainWindow", "更新", None))
                        self.setWindowTitle(_translate("MainWindow", "Hary", None))
                        self.trayIcon.setToolTip('Hary')
                        self.setStatus('无法联网或壁纸已损坏')
                # 或者当前更新间隔不为0，则开启线程按间隔时间更新壁纸
                else:
                    self.pushButton_1.setText(_translate("MainWindow", "停止", None))
                    self.setWindowTitle(_translate("MainWindow", "Hary - 正在自动更新壁纸", None))
                    self.trayIcon.setToolTip('Hary - 正在自动更新壁纸')
                    th = threading.Thread(target=cyc, name='wallpaper')
                    th.start()
            # 或者当前处于更新状态，则关闭更新状态
            else:
                self.pushButton_1.setText(_translate("MainWindow", "更新", None))
                self.setWindowTitle(_translate("MainWindow", "Hary", None))
                self.trayIcon.setToolTip('Hary')

    # 按分类获取壁纸
    def clsWallpaper(self):
        # 如果处于大图显示控件，则返回主页面
        if self.bigImg.isVisible():
            self.bigImg.setVisible(False)
            self.leftImg.setVisible(False)
            self.rightImg.setVisible(False)
            self.backImg.setVisible(False)
            self.wallImg.setVisible(False)
        # 重置壁纸更换下标
        Ui_MainWindow.__index = 0
        self.setStatus('正在加载壁纸')
        # 获取壁纸链接列表
        s1, h1 = ZolUrl.getAllWallpaperUrl(Ui_MainWindow.__di[self.comboBox_1.currentIndex()], Ui_MainWindow.__si[self.comboBox_2.currentIndex()], 1)
        # 如果壁纸链接列表小于20，则没有正常获取壁纸，并显示提示信息
        if len(s1) < 20:
            Ui_MainWindow.__img_url_s = [Ui_MainWindow.__path] * 20
            self.loadWallpaper()
            self.setStatus('无法联网或壁纸已损坏')
        # 或者正常获取壁纸链接列表，则加载图片，并显示提示信息
        else:
            Ui_MainWindow.__img_url_s, Ui_MainWindow.__img_url_h = s1, h1
            Ui_MainWindow.__status = self.comboBox_1.currentText() + '(' + Ui_MainWindow.__si[self.comboBox_2.currentIndex()] + ')'
            self.loadWallpaper()
            self.setStatus(Ui_MainWindow.__status)

    # 按随机获取壁纸
    def randomWallpaper(self):
        # 如果处于大图显示控件，则返回主页面
        if self.bigImg.isVisible():
            self.bigImg.setVisible(False)
            self.leftImg.setVisible(False)
            self.rightImg.setVisible(False)
            self.backImg.setVisible(False)
            self.wallImg.setVisible(False)
        # 重置壁纸更换下标
        Ui_MainWindow.__index = 0
        self.setStatus('正在加载壁纸')
        # 获取壁纸链接列表
        s1, h1 = ZolUrl.getAllWallpaperUrl(Ui_MainWindow.__di[random.randint(0, 21)], Ui_MainWindow.__si[self.comboBox_2.currentIndex()], random.randint(1, 5))
        # 如果壁纸链接列表小于20，则没有正常获取壁纸，并显示提示信息
        if len(s1) < 20:
            Ui_MainWindow.__img_url_s = [Ui_MainWindow.__path] * 20
            self.loadWallpaper()
            self.setStatus('无法联网或壁纸已损坏')
        # 或者正常获取壁纸链接列表，则加载图片，并显示提示信息
        else:
            Ui_MainWindow.__img_url_s, Ui_MainWindow.__img_url_h = s1, h1
            Ui_MainWindow.__status = '随机(' + Ui_MainWindow.__si[self.comboBox_2.currentIndex()] + ')'
            self.loadWallpaper()
            self.setStatus(Ui_MainWindow.__status)

    # 加载壁纸图片
    def loadWallpaper(self):
        self.webView_01.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[0])))
        self.webView_02.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[1])))
        self.webView_03.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[2])))
        self.webView_04.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[3])))
        self.webView_05.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[4])))
        self.webView_06.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[5])))
        self.webView_07.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[6])))
        self.webView_08.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[7])))
        self.webView_09.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[8])))
        self.webView_10.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[9])))
        self.webView_11.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[10])))
        self.webView_12.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[11])))
        self.webView_13.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[12])))
        self.webView_14.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[13])))
        self.webView_15.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[14])))
        self.webView_16.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[15])))
        self.webView_17.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[16])))
        self.webView_18.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[17])))
        self.webView_19.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[18])))
        self.webView_20.load(QtCore.QUrl(_fromUtf8(Ui_MainWindow.__img_url_s[19])))

    # 创建右键托盘菜单
    def createTrayMenu(self):
        # 退出程序，并关闭子进程
        def quitProgram():
            self.pushButton_1.setText(_translate("MainWindow", "更新", None))
            QtGui.qApp.quit()
        # 系统托盘图标
        img_open = QtGui.QIcon(r'D:\Hary\res\icon.ico')
        # 打开主面板
        self.restoreAction = QtGui.QAction(img_open, "打开主面板", self)
        self.restoreAction.triggered.connect(self.showWindow)
        # 退出
        self.quitAction = QtGui.QAction("退出", self)
        self.quitAction.triggered.connect(quitProgram)
        # 添加到菜单
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.quitAction)
        self.trayIcon.setContextMenu(self.trayIconMenu)

    # 打开主界面，并显示提示信息
    def showWindow(self):
        self.setStatus(Ui_MainWindow.__status)
        self.showNormal()
