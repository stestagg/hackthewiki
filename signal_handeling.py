import signal, os, sys, random

def handler(signum, frame):
	print("http://en.wikipedia.org/wiki/Jesus")
	print('***Jesus found!***')
	sys.exit(0)

def prepareToFindJesus():
	# Set the signal handler and a 5-second alarm
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(30 + random.randint(10, 20))

def jesusFound():
	signal.alarm(0)    # Disable the alarm

def main():
	start()

if __name__ == '__main__':
	main()
