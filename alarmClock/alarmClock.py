import subprocess
import time
from threading import Timer
import datetime

class playsound:
	def timerSound():
		audio = "./sounds/dead.wav"
		return_code = subprocess.call(["afplay", audio])
		return return_code

	def alarmSound():
		audio = "./sounds/delt_goblin-target.wav"
		return_code = subprocess.call(["afplay", audio])
		return return_code

class clock:

	# will display the current time
	def displayTime():
		print(time.ctime())
	#timer will count down from the given time
	# to display minutes and hours need to make seperate channels to deal with those
	def timer(timelen: int):
		start = time.time()
		totaltime = int(timelen - (time.time() - start))
		second = totaltime
		minutes = 00
		hours = 00
		if second >= 60:
			minutes = second // 60
			second %= 60
		if minutes >= 60:
			hours = minutes // 60
			minutes %= 60
		print ('%02d:%02d:%02d' % (hours, minutes, second))
		try:
			while time.time() - start < timelen:
				if (second == 0 and minutes > 0):
					second = 60
					minutes -= 1
				if (minutes == 0 and second == 0 and hours > 0):
					minutes = 60
					hours -= 1
				if (int(timelen - (time.time() - start)) < totaltime):
					totaltime = int(timelen - (time.time() - start))
					second -= 1
					print ('%02d:%02d:%02d' % (hours, minutes, second))
				time.sleep(0.2) # give the cpu that juicy break time :D
			for i in range(10):
				playsound.timerSound()
		except KeyboardInterrupt:
			print("timer deleted")

	#this one is threaded so we can run other things at the same time
	def timer2(timelen: int):
		try:
			Timer(timelen, playsound.timerSound, ()).start()
		except KeyboardInterrupt:
			print("timer deleted")

	#alarm will work like an alarm clock.
	# given a time in hour:minute format will alarm at the given time.
	# next step is to let the user use 12 hour format with AM PM specification
	# convert that to 23 hour format
	def alarm(mytime: str):
		ctime = time.strftime("%H:%M")
		print(ctime)
		print("alarm set for ", mytime)
		try:
			while ctime != mytime:
				time.sleep(1) # this makes it so we arent using all the cpu power checking the time as fast as possible
				ctime = time.strftime("%H:%M")
			for i in range(30):
				playsound.alarmSound()
		except KeyboardInterrupt:
			print("alarm deleted")


def main():
	clock.timer(71)
	#clock.alarm("00:22")
	clock.displayTime()
	#all the setup for the ui and the user input
	#determine whether the user wants to use the timer or set an alarm
	# would be cool to open a window and make a gui for this as well
	# need to learn how to repeat the play until stopped by the user
main()
