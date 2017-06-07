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

	#timer will count down from the given time
	# to display minutes and hours need to make seperate channels to deal with those
	#takes total number of seconds as parameter
	def timer(timelen: int):
		start = time.time()
		totaltime = int(timelen - (time.time() - start))
		second = totaltime
		minutes = 00
		hours = 00
		# convert seconds to minutes if needed
		if second >= 60:
			minutes = second // 60
			second %= 60
		# convert minutes to hours if needed
		if minutes >= 60:
			hours = minutes // 60
			minutes %= 60
		print ('%02d:%02d:%02d' % (hours, minutes, second))
		try:
			# current time - the time we started at count up to the tartet time.
			while time.time() - start < timelen:
				if (second == 0 and minutes > 0):
					second = 60
					minutes -= 1
				if (minutes == 0 and second == 0 and hours > 0):
					minutes = 60
					hours -= 1
				# if one second has passed
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
	def alarm(mytime: str):
		ctime = time.strftime("%H:%M")
		try:
			while ctime != mytime:
				time.sleep(1) # really only need to run once every second for this
				ctime = time.strftime("%H:%M")
			for i in range(30):
				playsound.alarmSound()
		except KeyboardInterrupt:
			print("alarm deleted")
