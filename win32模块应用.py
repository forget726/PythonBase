import time
import win32api
import win32con
from ctypes import *
import multiprocessing
import os


def block(delay_time, block_time):
    """禁用键盘鼠标"""
    print(os.getpid())
    time.sleep(delay_time)  # 启动延迟
    windll.user32.BlockInput(True)  # 禁用键盘鼠标
    time.sleep(block_time)  # 锁定时间


def press_event(key_value, times):
    """输入事件,指定次数，每次时间间隔0.2s"""
    time.sleep(1)
    print(os.getpid())
    for i in range(times):
        win32api.keybd_event(key_value, 0, 0, 0)
        win32api.keybd_event(key_value, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(0.2)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=block, args=(2, 20))
    p2 = multiprocessing.Process(target=press_event, args=(77, 50))
    p2.start()
    p1.start()
