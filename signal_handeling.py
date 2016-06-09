import signal, os, sys

def handler(signum, frame):
	print("https://en.wikipedia.org/wiki/Jesus")
	print('***Jesus found!***')
	sys.exit(0)

def prepareToFindJesus():
	# Set the signal handler and a 5-second alarm
	signal.signal(signal.SIGALRM, handler)
	signal.alarm(5)

def jesusFound():
	signal.alarm(0)    # Disable the alarm

def main():
	print 'starting'
	start()
	while True:
		a= 1+1

if __name__ == '__main__':
	main()
