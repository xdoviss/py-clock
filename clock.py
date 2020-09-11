import time
import os
import sys
import winsound
from datetime import datetime

x = 0
dateParam = '%Y-%m-%d %H:%M:%S'
ticks = 0
timerLength = 5

def clear():
	os.system('cls')

def startMsg():
	print('Type "clock" to start the clock, "timer" to start timer, "stopwatch" to start stopwatch "settings" to change clock settings.')

def timer():
	global ticks
	timerHrs, timerMins, timerSecs = input('Input timer length separated by commas (hours, minutes, seconds): ').split(',')
	timerLength = int(timerHrs) * 60 * 60 + int(timerMins) * 60 + int(timerSecs)
	while ticks < int(timerLength):
		clear()
		ticks += 1
		print('Timer length: ' + str(timerLength) + 's')
		print('------------------------')
		print('Time passed: ' + str(ticks) + 's')
		print('Time left: ' + str(int(timerLength) - int(ticks)) + 's')
		time.sleep(1)
	if int(ticks) == int(timerLength):
		winsound.PlaySound('radarAlarm', winsound.SND_FILENAME)

def stopwatch():
	timePassed = 0
	while x == 0:
		try:
			clear()
			timePassed += 1
			print('Time passed: ' + str(timePassed) + 's (CTRL + C to stop)')
			time.sleep(1)
		except KeyboardInterrupt:
			clear()
			print('Total time: ' + str(timePassed) + 's')
			break

def clock():
	while x == 0:
		clear()
		print(datetime.now().strftime(dateParam))
		time.sleep(1)

def settings():
	global dateParam

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

def system():
	startMsg()
	inputString = input()

	if inputString == 'clock':
		clock()
	elif inputString == 'settings':
		settings()
	elif inputString == 'timer':
		timer()
	elif inputString == 'stopwatch':
		stopwatch()
	else:
		print('Invalid Input.')
		system()

system()