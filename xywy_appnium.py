#coding=utf-8
import os
import time
import unittest
from appium import webdriver
global driver


class Test_appnium:
	def __init__(self):
		desired_caps={
		'device':'android',
		'platformName':'Android',
		'browserName':'',
		'version':'6.0',
		'deviceName':'MYV0215627013610',
		'appPackage':'com.xywy.askxywy',
		'appActivity':'.domain.welcome.activity.WelcomeActivity',
		'unicodeKeyboard':True,
		'resetKeyboard':True
		}
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
		time.sleep(5)
		self.driver.implicitly_wait(1)

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
		return self.driver.find_elements_by_id(id)

	def fid(self, id):
		return self.driver.find_element_by_id(id)

class phone(Test_appnium):
	def actions(self):
		# self.swipLeft(1000)
		# time.sleep(1)
		# self.swipRight(1000)
		# time.sleep(1)
		# self.swipeUp(1000)
		# time.sleep(1)
		# self.swipeDown(1000)
		account = '17810354797'
		passwd = 'test123'
		input_massage = '最近有点感冒发烧嗓子疼怎么办啊医生，很久了'.decode('utf-8')

		#登陆
		self.fid('com.xywy.askxywy:id/tabMine').click()
		#判断登陆
		try:
			logined = self.fid('com.xywy.askxywy:id/tv_title_mine')
		except:
			#未登陆，登陆
			account_pwd = self.fids('com.xywy.askxywy:id/input_edit_text')
			account_pwd[0].send_keys(account)
			account_pwd[1].send_keys(passwd)
			self.fid('com.xywy.askxywy:id/login_btn_tv').click()
		else:
			#已登陆，跳过
			self.fid('com.xywy.askxywy:id/tabQuery').click()

		
		#快速问诊
		self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
		self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage)
		self.fid('com.xywy.askxywy:id/btn_right').click()


if __name__ == '__main__':
	myphone = phone()
	myphone.actions()
