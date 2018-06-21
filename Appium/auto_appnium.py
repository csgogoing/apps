#coding=utf-8
import os
import re
import time
from appium import webdriver
global driver
import random


class Test_appnium:
	def __init__(self):
		# 读取设备 id
		readDeviceId = list(os.popen('adb devices').readlines())
		# 正则表达式匹配出 id 信息
		deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
		#设备信息
		desired_caps={
		'newCommandTimeout':60,
		'device':'android',
		'platformName':'Android',
		'browserName':'',
		'version':'',
		'deviceName':deviceId,
		'appPackage':'com.xywy.askxywy',
		'appActivity':'.domain.welcome.activity.WelcomeActivity',
		'unicodeKeyboard':True,
		'resetKeyboard':True
		}
		#打开webdriver，重试3次
		maxTryNum=3
		for tries in range(maxTryNum):
			try:	
				self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
				break
			except:
				if tries < (maxTryNum-1):
					print("重试第%d次") %maxTryNum
					continue
				else:
					print('启动webdriver失败')
			else:
				logging.error("Has tried %d times, all failed!",maxTryNum)
				break
		time.sleep(5)
		self.driver.implicitly_wait(2)
		print("程序启动完毕")

	#获得机器屏幕大小x,y
	def getSize(self):
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		return (x, y)

	#屏幕向上滑动
	def swipeUp(self, t):
		l = self.getSize()
		x1 = int(l[0] * 0.5)  #x坐标
		y1 = int(l[1] * 0.75)   #起始y坐标
		y2 = int(l[1] * 0.25)   #终点y坐标
		self.driver.swipe(x1, y1, x1, y2,t)
	#屏幕向下滑动
	def swipeDown(self, t):
		l = self.getSize()
		x1 = int(l[0] * 0.5)  #x坐标
		y1 = int(l[1] * 0.25)   #起始y坐标
		y2 = int(l[1] * 0.75)   #终点y坐标
		self.driver.swipe(x1, y1, x1, y2,t)
	#屏幕向左滑动
	def swipLeft(self, t):
		l= self.getSize()
		x1=int(l[0]*0.75)
		y1=int(l[1]*0.5)
		x2=int(l[0]*0.05)
		self.driver.swipe(x1,y1,x2,y1,t)
	#屏幕向右滑动
	def swipRight(self, t):
		l= self.getSize()
		x1=int(l[0]*0.05)
		y1=int(l[1]*0.5)
		x2=int(l[0]*0.75)
		self.driver.swipe(x1,y1,x2,y1,t)

	def fids(self, id):
		#ID查找元素方法
		return self.driver.find_elements_by_id(id)

	def fid(self, id):
		#ID查找元素方法
		return self.driver.find_element_by_id(id)

	def mquit(self):
		#退出driver
		self.driver.quit()
		print('程序退出')
