#因为APUS桌面软件用UI AOTUMATION检测不到任何可以直接查询到的控件属性，只有空间位置，于是我只好寻找直接模拟手指点击的方式去进行操作
#代码如下

#coding=utf-8
import os
import time
import unittest
from appium import webdriver
global driver

 

class LoginAndroidTests(unittest.TestCase):

    def setUp(self):

        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'
        desired_caps['browserName']=''
        desired_caps['version']='4.4.2'
        desired_caps['deviceName']='BY2QUX14AP047580'
        desired_caps['appPackage']='com.apusapps.launcher'
        desired_caps['appActivity']='.launcher.ApusLauncherActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

       

    def tearDown(self):
        pass
   

    def test_login(self):
        time.sleep(5)
        #self.driver.swipe(100,500,500,500,5)
	#获得机器屏幕大小x,y
	def getSize():
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		return (x, y)
	 
	#屏幕向上滑动
	def swipeUp(t):
		l = getSize()
		x1 = int(l[0] * 0.5)  #x坐标
		y1 = int(l[1] * 0.75)   #起始y坐标
		y2 = int(l[1] * 0.25)   #终点y坐标
		self.driver.swipe(x1, y1, x1, y2,t)
	#屏幕向下滑动
	def swipeDown(t):
		l = getSize()
		x1 = int(l[0] * 0.5)  #x坐标
		y1 = int(l[1] * 0.25)   #起始y坐标
		y2 = int(l[1] * 0.75)   #终点y坐标
		self.driver.swipe(x1, y1, x1, y2,t)
	#屏幕向左滑动
	def swipLeft(t):
		l=getSize()
		x1=int(l[0]*0.75)
		y1=int(l[1]*0.5)
		x2=int(l[0]*0.05)
		self.driver.swipe(x1,y1,x2,y1,t)
	#屏幕向右滑动
	def swipRight(t):
		l=getSize()
		x1=int(l[0]*0.05)
		y1=int(l[1]*0.5)
		x2=int(l[0]*0.75)
		self.driver.swipe(x1,y1,x2,y1,t)
	#调用向左滑动
	swipLeft(1000)
	time.sleep(3)
	#调用向右滑动
	swipRight(1000)
	调用向上滑动
	swipeUp(1000)
	调用向下滑动
	swipeDown(1000)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
