import time
import os
import sys
from sys import platform
import winsound
from datetime import datetime

x = 0
dateParam = '%Y-%m-%d %H:%M:%S'
ticks = 0
timerLength = 5

def clear():
	if platform == 'linux' or platform == 'linux2':
		os.system("echo 'clear'")
	elif platform == 'darwin':
		os.system("echo 'clear'")
	else:
		os.system('cls')


def startMsg():
	print('Commands:\n"clock" to start the clock,\n"timer" to start timer,\n"stopwatch" to start stopwatch,\n"alarm" to set an alarm,\n"settings" to change clock settings.\n[Pressing Ctrl + C brings you back to this menu.]')

def timer():
	clear()
	global ticks
	timerHrs, timerMins, timerSecs = input('Input timer length separated by commas (hours, minutes, seconds): ').split(',')
	timerLength = int(timerHrs) * 60 * 60 + int(timerMins) * 60 + int(timerSecs)
	while ticks < int(timerLength):
		try:
			clear()
			ticks += 1
			print('Timer length: ' + str(timerLength) + 's')
			print('------------------------')
			print('Time passed: ' + str(ticks) + 's')
			print('Time left: ' + str(int(timerLength) - int(ticks)) + 's')
			time.sleep(1)
		except KeyboardInterrupt:
			clear()
			system()
	if int(ticks) == int(timerLength):
		winsound.PlaySound('radarAlarm', winsound.SND_FILENAME)

def alarm():
	clear()
	alarmTime = input('Input time when alarm should go off (hours:minutes): ')
	clear()
	print('Alarm will play at ' + alarmTime)
	while True:
		try:
			if datetime.now().strftime('%H:%M') == alarmTime:
				print('It is now: ' + alarmTime)
				winsound.PlaySound('radarAlarm', winsound.SND_FILENAME)
				break
			else:
				pass
		except KeyboardInterrupt:
			clear()
			system()

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
	print('\nType "menu" to go back to menu.')
	goMenu = input()
	if goMenu == 'menu':
		clear()
		system()

def clock():
	while x == 0:
		try:
			clear()
			print(datetime.now().strftime(dateParam))
			time.sleep(1)
		except KeyboardInterrupt:
			clear()
			system()
			
def settings():
	clear()
	global dateParam

	print('1 - full date\n2 - hours, minutes, seconds\n3 - minutes, seconds')
	inputOfSetting = input()

	if inputOfSetting == '1':
		clear()
		system()
	elif inputOfSetting == '2':
		dateParam = '%H:%M:%S'
		clear()
		system()
	elif inputOfSetting == '3':
		dateParam = '%M:%S'
		clear()
		system()
	elif KeyboardInterrupt:
		clear()
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
	elif inputString == 'alarm':
		alarm()
	else:
		print('Invalid Input.')
		system()

system()