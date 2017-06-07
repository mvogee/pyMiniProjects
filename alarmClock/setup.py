from alarmClock import clock

class setup:

	def timer():
		print("\nussage: hours:minutes:seconds\n\"00:00:00\"\n")
		time_length = input("enter timer: ")
		try:
			# abstract the hours, minutes, and seconds from input
			hours = int(time_length[0:2])
			minutes = int(time_length[3:5])
			seconds = int(time_length[6:8])
			# convert all time lengths to seconds for total time 
			totalseconds = seconds + (minutes * 60) + (hours * 3600)
			print("timer set for", time_length)
			start = input("type start to start or anything else to exit: ")
			if (start.lower() == "start"):
				clock.timer(totalseconds)
			else:
				return
		except:
			print("please use the format 00:00:00\n")

	def alarm():
		print ("ussage: hour:minute AM/PM\n\"07:30AM\"\n")
		alarm_time = input("enter alarm time: ")
		#save the original input string to display once the conversion is done
		savetime = alarm_time
		try:
			#make sure the format is correct
			if (int(alarm_time[0:2]) <= 12 and int(alarm_time[3:5]) < 60):
				if (alarm_time[5:7].lower() == "am"):
					#12 am is the only time we modify AM time
					if (alarm_time[0:2] == "12"):
						alarm_time = "00" + alarm_time[2:]
				elif (alarm_time[5:7].lower() == "pm"):
						#noon is the only time we do not add 12 hours to the total
						if (not(alarm_time[0:2] == "12")):
							alarmt = int(alarm_time[0:2]) + 12
							alarm_time = str(alarmt) + alarm_time[2:]
				#abstract the real time cutting off the AM or PM
				alarm_time = alarm_time[0:5]
				print("alarm set for: ", savetime)
				clock.alarm(alarm_time);
			else:
				print("please use the format 12:59AM")
		except:
			print("please use the format 12:59AM")
