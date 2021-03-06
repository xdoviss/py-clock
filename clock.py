import time
import os
import sys
from sys import platform
import winsound
from datetime import datetime
import re

x = 0
dateParam = '%H %M %S'
ticks = 0
timerLength = 5

block = [
	['████', '█  █', '█  █', '█  █', '████'], #0
	[' ██ ', '  █ ', '  █ ', '  █ ', ' ███'], #1
	['████', '   █', '████', '█   ', '████'], #2
	['████', '   █', '████', '   █', '████'], #3
	['█  █', '█  █', '████', '   █', '   █'], #4
	['████', '█   ', '████', '   █', '████'], #5
	['████', '█   ', '████', '█  █', '████'], #6
	['████', '   █', '   █', '   █', '   █'], #7
	['████', '█  █', '████', '█  █', '████'], #8
	['████', '█  █', '████', '   █', '████'] #9
]

line = [
	['┏━━┓', '┃  ┃', '┃  ┃', '┃  ┃', '┗━━┛'],
	[' ━┓ ', '  ┃ ', '  ┃ ', '  ┃ ', ' ━┻━'],
	['┏━━┓', '   ┃', '┏━━┛', '┃   ', '┗━━━'],
	['━━━┓', '   ┃', '━━━┫', '   ┃', '━━━┛'],
	['╻  ╻', '┃  ┃', '┗━━┫', '   ┃', '   ╹'],
	['┏━━━', '┃   ', '┗━━┓', '   ┃', '━━━┛'],
	['┏━━┓', '┃   ', '┣━━┓', '┃  ┃', '┗━━┛'],
	['━━━┓', '   ┃', '   ┃', '   ┃', '   ╹'],
	['┏━━┓', '┃  ┃', '┣━━┫', '┃  ┃', '┗━━┛'],
	['┏━━┓', '┃  ┃', '┗━━┫', '   ┃', '┗━━┛']
]

double = [
	['╔══╗', '║  ║', '║  ║', '║  ║', '╚══╝'],
	[' ═╗ ', '  ║ ', '  ║ ', '  ║ ', ' ═╩═'],
	['╔══╗', '   ║', '╔══╝', '║   ', '╚═══'],
	['═══╗', '   ║', '═══╣', '   ║', '═══╝'],
	['║  ║', '║  ║', '╚══╣', '   ║', '   ║'],
	['╔═══', '║   ', '╚══╗', '   ║', '═══╝'],
	['╔══╗', '║   ', '╠══╗', '║  ║', '╚══╝'],
	['═══╗', '   ║', '   ║', '   ║', '   ║'],
	['╔══╗', '║  ║', '╠══╣', '║  ║', '╚══╝'],
	['╔══╗', '║  ║', '╚══╣', '   ║', '╚══╝']
]

colon = [
	['    ', ' █  ', '    ', ' █  ', '    '],
	['    ', ' ┃  ', '    ', ' ┃  ', '    '],
	['    ', ' ║  ', '    ', ' ║  ', '    ']
]

font = block
clnFont = 0

def printTime():
	theTime = datetime.now().strftime(dateParam)

	def split(theTime):
		return [char for char in theTime]

	timeRn = split(theTime)

	print(font[int(timeRn[0])][0] + ' ' + font[int(timeRn[1])][0] + ' ' + colon[clnFont][0] + ' ' + font[int(timeRn[3])][0] + ' ' + font[int(timeRn[4])][0] + ' ' + colon[clnFont][0] + ' ' + font[int(timeRn[6])][0] + ' ' + font[int(timeRn[7])][0])
	print(font[int(timeRn[0])][1] + ' ' + font[int(timeRn[1])][1] + ' ' + colon[clnFont][1] + ' ' + font[int(timeRn[3])][1] + ' ' + font[int(timeRn[4])][1] + ' ' + colon[clnFont][1] + ' ' + font[int(timeRn[6])][1] + ' ' + font[int(timeRn[7])][1])
	print(font[int(timeRn[0])][2] + ' ' + font[int(timeRn[1])][2] + ' ' + colon[clnFont][2] + ' ' + font[int(timeRn[3])][2] + ' ' + font[int(timeRn[4])][2] + ' ' + colon[clnFont][2] + ' ' + font[int(timeRn[6])][2] + ' ' + font[int(timeRn[7])][2])
	print(font[int(timeRn[0])][3] + ' ' + font[int(timeRn[1])][3] + ' ' + colon[clnFont][3] + ' ' + font[int(timeRn[3])][3] + ' ' + font[int(timeRn[4])][3] + ' ' + colon[clnFont][3] + ' ' + font[int(timeRn[6])][3] + ' ' + font[int(timeRn[7])][3])
	print(font[int(timeRn[0])][4] + ' ' + font[int(timeRn[1])][4] + ' ' + colon[clnFont][4] + ' ' + font[int(timeRn[3])][4] + ' ' + font[int(timeRn[4])][4] + ' ' + colon[clnFont][4] + ' ' + font[int(timeRn[6])][4] + ' ' + font[int(timeRn[7])][4])

def clear():
	if platform == 'linux' or platform == 'linux2':
		os.system('clear')
	elif platform == 'darwin':
		os.system('clear')
	else:
		os.system('cls')


def startMsg():
	print('Commands:\n"clock" to start the clock,\n"timer" to start timer,\n"stopwatch" to start stopwatch,\n"alarm" to set an alarm,\n"fonts" to change clock font.\n[Pressing Ctrl + C brings you back to this menu.]')

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
		winsound.PlaySound('radarAlarm.wav', winsound.SND_FILENAME)

def alarm():
	clear()
	alarmTime = input('Input time when alarm should go off (hours:minutes): ')
	clear()
	print('Alarm will play at ' + alarmTime)
	while True:
		try:
			if datetime.now().strftime('%H:%M') == alarmTime:
				print('It is now: ' + alarmTime)
				winsound.PlaySound('radarAlarm.wav', winsound.SND_FILENAME)
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
			printTime()
			time.sleep(1)
		except KeyboardInterrupt:
			clear()
			system()
			
def fonts():
	clear()
	global font
	global clnFont
	print('1 - block █\n2 - line ┃\n3 - double ║')
	inputOfFont = input()

	if inputOfFont == '1':
		font = block
		clnFont = 0
		clear()
		system()
	elif inputOfFont == '2':
		font = line
		clnFont = 1
		clear()
		system()
	elif inputOfFont == '3':
		font = double
		clnFont = 2
		clear()
		system()
	else:
		print('Invalid Input.')
		clear()
		system()

def system():
	os.system('mode con: cols=50 lines=8')
	startMsg()
	inputString = input()

	if inputString == 'clock':
		clock()
	elif inputString == 'fonts':
		fonts()
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