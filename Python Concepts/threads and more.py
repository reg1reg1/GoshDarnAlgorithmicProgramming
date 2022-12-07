'''
Written in notion for python2
Using target notation for threads
'''
import threading
import os
import subprocess
import time


def fun_daemon():
	print("Daemon thread started")
	time.sleep(5)
	subprocess.check_output("notepad.exe",shell=True)
	print("I may never get displayed")


def fun_nondaemon():
	print("non daemon thread started")
	for i in range(1,500):
		print("Non daemon Iteration:",i)
	print("Non daemon thread ended")

print("Main thread started")
#calling thread by passing argument to the constructor
t1 = threading.Thread(target=fun_daemon)
t2 = threading.Thread(target=fun_nondaemon)
t1.setDaemon(True)
t1.start()
t2.start()
for x in xrange(1,10):
	print("Main thread in iteration ", x)

