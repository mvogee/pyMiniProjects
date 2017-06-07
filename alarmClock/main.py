#from alarmClock import clock
from setup import setup

def display_ussage():
	print("""available commands:
	timer
	alarm
	quit
	HELP""")

def main():
	print("welcome to miniClock\n")
	while 1:
		userin = input("\nEnter what you would like to use or HELP for ussage: ")
		userin = userin.lower();
		if (userin == "help"):
			display_ussage()
		elif (userin == "quit"):
			break ;
		elif (userin == "timer"):
			setup.timer()
		elif (userin == "alarm"):
			setup.alarm()
		else:
			print("unknown command\n")

main()
