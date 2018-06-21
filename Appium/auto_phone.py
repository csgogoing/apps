#coding=utf-8
from auto_appnium import Test_appnium
import time
import random

class phone(Test_appnium):
	def __init__(self):
		super(phone, self).__init__()
		#登陆
		account = '17810354797'
		passwd = 'test123'
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
		print("登陆完毕")

	def actions(self, choose):
		# self.swipLeft(1000)
		input_massage = "最近感冒发烧嗓子疼，怎么办啊医生，很久了"
		for i in range(3):
			try:
				self.fid('com.xywy.askxywy:id/quick_ask_layout')
			except:
				self.driver.keyevent('4') 
				time.sleep(1)
				continue
			else:
				break
		if choose == 1:
			#快速问诊
			self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
			#输入内容
			self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage+"杜军医生%d" %random.randrange(1,100,1))
			time.sleep(1)
			#下一步
			self.fid('com.xywy.askxywy:id/btn_right').click()
			for i in range(1,4):
				try:
					dujun = self.driver.find_element_by_android_uiautomator('new UiSelector().text("杜军")')
				except:
					pass
				else:
					dujun.click()
					temp = 1
					break
			if temp == 1:
				self.fid('com.xywy.askxywy:id/btn_commit').click()
				print("""创建杜军医生订单成功
					""")
			else:
				print("""没有找到杜军医生，创建订单失败
					""")

		elif choose == 2:
			#快速问诊
			self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
			#输入内容
			self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage+"3元%d" %random.randrange(1,100,1))
			time.sleep(1)
			#下一步
			self.fid('com.xywy.askxywy:id/btn_right').click()
			#选择悬赏提问
			self.fid('com.xywy.askxywy:id/reward_text').click()
			self.fid('com.xywy.askxywy:id/submitBtn').click()
			self.driver.find_element_by_android_uiautomator('new UiSelector().text("将有医生为您快速解答")').click()
			#提交问题
			self.fid('com.xywy.askxywy:id/btn_commit').click()
			print("""创建3元医生订单成功
				""")

		elif choose == 3:
			#快速问诊
			self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
			#输入内容
			self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage+"5元%d" %random.randrange(1,100,1))
			time.sleep(1)
			#下一步
			self.fid('com.xywy.askxywy:id/btn_right').click()
			#选择悬赏提问
			self.fid('com.xywy.askxywy:id/reward_text').click()
			self.fid('com.xywy.askxywy:id/submitBtn').click()
			self.driver.find_element_by_android_uiautomator('new UiSelector().text("二甲及以上级别医生为您服务")').click()
			#提交问题
			#self.fid('com.xywy.askxywy:id/btn_commit').click()
			print("""创建5元医生订单成功
				""")

		elif choose == 4:
			#快速问诊
			self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
			#输入内容
			self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage+"10元%d" %random.randrange(1,100,1))
			time.sleep(1)
			#下一步
			self.fid('com.xywy.askxywy:id/btn_right').click()
			#选择悬赏提问
			self.fid('com.xywy.askxywy:id/reward_text').click()
			self.fid('com.xywy.askxywy:id/submitBtn').click()
			self.driver.find_element_by_android_uiautomator('new UiSelector().text("二甲医院以上级别医生为您解答")').click()
			#提交问题
			self.fid('com.xywy.askxywy:id/btn_commit').click()
			print("""创建10元医生订单成功
				""")

		elif choose == 5:
			#快速问诊
			self.fid('com.xywy.askxywy:id/quick_ask_layout').click()
			#输入内容
			self.fid('com.xywy.askxywy:id/et_question_describe').send_keys(input_massage+"免费%d" %random.randrange(1,100,1))
			time.sleep(1)
			#下一步
			self.fid('com.xywy.askxywy:id/btn_right').click()
			#选择悬赏提问
			self.fid('com.xywy.askxywy:id/reward_text').click()
			self.fid('com.xywy.askxywy:id/submitBtn').click()
			#点击免费提问
			self.fid('com.xywy.askxywy:id/reward_skip_to_ask').click()
			print("""创建免费订单成功
				""")

		else:
			print("输入函数错误，创建订单失败")

