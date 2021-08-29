# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:49:28 2021

@author: admin
"""

#对后台窗口截图

import win32gui, win32ui, win32con
import cv2
import numpy

def u(hWnd = 0):
       #获取后台窗口的句柄，注意后台窗口不能最小化
    left, top, right, bot = win32gui.GetWindowRect(hWnd)
    width = right - left
    height = bot - top
    hWndDC = win32gui.GetWindowDC(hWnd)#返回句柄窗口的设备环境，覆盖整个窗口，包括非客户区，标题栏，菜单，边框
    mfcDC = win32ui.CreateDCFromHandle(hWndDC)#创建设备描述表
    saveDC = mfcDC.CreateCompatibleDC()#创建内存设备描述表
    saveBitMap = win32ui.CreateBitmap()#创建位图对象准备保存图片
    saveBitMap.CreateCompatibleBitmap(mfcDC,width,height)#为bitmap开辟存储空间
    saveDC.SelectObject(saveBitMap)#将截图保存到saveBitMap中
    saveDC.BitBlt((0,0), (width,height), mfcDC, (0, 0), win32con.SRCCOPY)#保存bitmap到内存设备描述表
    signedIntsArray = saveBitMap.GetBitmapBits(True)###获取位图信息
    win32gui.DeleteObject(saveBitMap.GetHandle())#内存释放
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hWnd,hWndDC)
    im_opencv = numpy.frombuffer(signedIntsArray, dtype = 'uint8')#显示到屏幕
    im_opencv.shape = (height, width, 4)
    cv2.cvtColor(im_opencv, cv2.COLOR_BGRA2RGB)
    return  im_opencv



im_opencv=u(854182)  

cv2.namedWindow('im_opencv') #命名窗口
cv2.imshow("im_opencv",im_opencv) #显示
cv2.waitKey(0)
cv2.destroyAllWindows()

