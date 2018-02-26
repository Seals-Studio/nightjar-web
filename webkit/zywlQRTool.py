#!/usr/bin/env python  
# _*_ coding:utf-8 _*_  
#  
# @Version : 1.0  
# @Time    : 2018-2-26
# @Author  : liupan
# @File    : zywlQRTool.py  
#  
# 智影未来二维码扫描webkit

import webview
webview.create_window("智影未来二维码桌面扫描版", "http://localhost:9090/nightjar", fullscreen=True, resizable=True, background_color='#303133')
