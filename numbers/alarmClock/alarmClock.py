import subprocess
import time
from threading import Timer

class playsound:
	def timerSound():
		audio = "./sounds/dead.wav"
		return_code = subprocess.call(["afplay", audio])
		return return_code

	def alarmSound():
		audio = "./sounds/delt_goblin-target.wav"
		return_code = subprecess.call(["afplay", audio])
		return return_code

class clock:

	# will display the current time
	def displayTime():
		print(time.ctime())
	#timer will count down from the given time
	# to display minutes and hours need to make seperate channels to deal with those
	def timer(timelen: int):
		start = time.time()
		second = int(timelen - (time.time() - start)) + 1
		print (second)
		try:
			while time.time() - start < timelen:
				if (int(timelen - (time.time() - start)) + 1 < second):
					second = int(timelen - (time.time() - start)) + 1
					print (second)
			print (0)
			for i in range(10):
				playsound.timerSound()
		except KeyboardInterrupt:
			return

	#this one is threaded so we can run other things at the exact same time
	def timer2(timelen: int):
		try:
			Timer(timelen, playsound.timerSound, ()).start()
		except KeyboardInterrupt:
			return
	#alarm will work like an alarm clock.
	def alarm(time: int):
		pass
		# how should i accept the time and date?
		# 6 - 12 pm or am. alwasy the upcomming day?


def main():
	pass
	#all the setup for the ui and the user input
	#determine whether the user wants to use the timer or set an alarm
	# would be cool to open a window and make a gui for this as well
	# need to learn how to repeat the play until stopped by the user
clock.timer(5)
clock.displayTime()
