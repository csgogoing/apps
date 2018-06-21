#coding=utf-8
from auto_phone import phone

if __name__ == '__main__':
	myphone = phone()
	while True:
		try:
			choose = int(input('''请选择要创建的问题类型：
				1：杜军医生指定问题
				2：3元悬赏问题
				3：5元悬赏问题
				4：10元悬赏问题
				5：免费问题
				Others：关闭
请选择：'''))
		except:
			myphone.mquit()
			break
		else:
			if choose in range(1,6):
				myphone.actions(choose)
			else:
				myphone.mquit()
				break
