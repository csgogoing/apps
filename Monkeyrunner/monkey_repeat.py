#!/usr/bin/env monkeyrunner
#coding=utf-8

import sys  
from com.android.monkeyrunner import MonkeyRunner
from com.android.monkeyrunner import MonkeyDevice
from com.android.monkeyrunner import MonkeyImage

CMD_MAP = {  
	'TOUCH': lambda dev, arg: dev.touch(**arg),  
	'DRAG': lambda dev, arg: dev.drag(**arg),  
	'PRESS': lambda dev, arg: dev.press(**arg),  
	'TYPE': lambda dev, arg: dev.type(**arg),  
	'WAIT': lambda dev, arg: MonkeyRunner.sleep(**arg)  
	}  
# Process a single file for the specified device.  
def process_file(fp, device, times):  
	for i in range(0,times):
		print 'run %d time' %i
		for line in fp:  
			(cmd, rest) = line.split('|')  
			try:
				# Parse the pydict  
				rest = eval(rest)  
			except:  
				print 'unable to parse options'  
				continue   
			if cmd not in CMD_MAP:  
				print 'unknown command: ' + cmd  
				continue   
			CMD_MAP[cmd](device, rest)
		fp.seek(0)
def main(): 
	file = sys.argv[1]
	try:
		times = int(sys.argv[2])
	except IndexError:
		times = 1
	fp = open(file, 'r')   
	device = MonkeyRunner.waitForConnection()
	print 'attach'
	device.startActivity(component="com.xywy.askxywy/.domain.welcome.activity.WelcomeActivity")
	MonkeyRunner.sleep(5)
	print 'begin'
	process_file(fp, device ,times)
	result = device.takeSnapshot()
	result.writeToFile('E:\\Mine\\Program\\Test_result.png','png')
	print 'success'  
	fp.close();	 
if __name__ == '__main__':  
	main()  