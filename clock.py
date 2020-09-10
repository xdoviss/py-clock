import time
import os
import sys
from datetime import datetime

x = 0
dateParam = '%Y-%m-%d %H:%M:%S'

def clear():
	os.system('cls')

def startMsg():
	print('Type "start" to start the clock, type "settings" to change clock settings.')
	print('[CURRENTLY CLOCK CANNOT BE STOPPED!]')

def system():
	global dateParam
	startMsg()
	inputString = input()

	if inputString == 'start':
		while x == 0:
			clear()
			print(datetime.now().strftime(dateParam))
			time.sleep(1)
	elif inputString == 'settings':
		print('1 - full date\n2 - hours, minutes, seconds\n3 - minutes, seconds')
		inputOfSetting = input()
		if inputOfSetting == '1':
			system()
		elif inputOfSetting == '2':
			dateParam = '%H:%M:%S'
			system()
		elif inputOfSetting == '3':
			dateParam = '%M:%S'
			system()
		else:
			print('Invalid Input.')
			system()
	else:
		print('Invalid Input.')
		system()

system()