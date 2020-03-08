"""调用API函数,模拟鼠标移动和点击的模块。
示例:
#使用Aero Peek预览桌面。
from event import mouse
x,y=mouse.get_screensize()
mouse.move(x,y) #将鼠标移至屏幕右下角
mouse.click() #模拟鼠标点击
"""
import time
from ctypes import *

__all__=["get_screensize","getpos","move","click","right_click","dblclick"]

#API常量
MOUSEEVENTF_LEFTDOWN = 0x2
MOUSEEVENTF_LEFTUP = 0x4

MOUSEEVENTF_MIDDLEDOWN = 0x20
MOUSEEVENTF_MIDDLEUP = 0x40 

MOUSEEVENTF_RIGHTDOWN = 0x8
MOUSEEVENTF_RIGHTUP = 0x10 

MOUSEEVENTF_MOVE = 0x1

user32=windll.user32

class PointAPI(Structure):
    #PointAPI类型,用于获取鼠标坐标
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def get_screensize():
    "获取当前屏幕分辨率。"
    GetSystemMetrics = user32.GetSystemMetrics
    return GetSystemMetrics(0), GetSystemMetrics(1)

def getpos():
    """获取当前鼠标位置。
返回值为一个元组,以(x,y)形式表示。"""
    po = PointAPI()
    user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)

def goto(x,y):
    "将鼠标移动至指定位置(x,y)。"
    user32.SetCursorPos(x,y)

def move(x,y):
    """模拟移动鼠标。
与goto不同,move()*产生*一个鼠标事件。"""
    user32.mouse_event(MOUSEEVENTF_MOVE,x,y)

def click():
    "模拟鼠标左键单击"
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN)
    user32.mouse_event(MOUSEEVENTF_LEFTUP)

def right_click():
    "模拟鼠标右键单击"
    user32.mouse_event(MOUSEEVENTF_LEFTDOWN)
    user32.mouse_event(MOUSEEVENTF_LEFTUP)

def dblclick(delay=0.25):
    "模拟鼠标左键双击"
    click()
    time.sleep(delay)
    click()