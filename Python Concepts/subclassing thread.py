'''
Python 2
Subclassing thread ( one may also use target method)
Using it to solve interthreading problems
Parallel implementation of segmented sieve
Python 3 has an advanced threading module
which works differently
'''
import sys
import getopt
import Queue
import threading
import time
import math

start = 1
end = -1
hashlist=[]

class PrimeSieve(threading.Thread):
	def __init__(self,queue,tid):
		#threading has to be inherited in old style way ( so no super)
		threading.Thread.__init__(self)
		self.tid=tid
		self.queue=queue
	 #Overrriding the run method of the superclass
	 
	def run(self):
		#The thread must continuously fetch from queue a number and then keep slicing it out
		global hashlist
		global end

		while True:
			try:
				num = self.queue.get(timeout=1)
				str1= "Fetched number-" + str(num)
				print str1
				if(hashlist[num]==1):
					self.queue.task_done()
					continue
				div = int (end/num)
				vstart = div*num
				print vstart
				for i in range(vstart,end,num):
					hashlist[i-vstart]=1
				self.queue.task_done()
			except Queue.Empty as e:
				str1= "Thread-" + str(self.tid)+" exiting..."
				print str1
				return
			
def main():
	global end
	global hashlist
	#options that require an argument are followed by a colon,
	#it just means that they require an argument to be passed as a value
	#The reinforcement that some options need to be set needs to be manually done by the programmer
	print sys.argv
	try:
		opt,arg=getopt.getopt(sys.argv[1:],"s:e:",["start","end"])
		if len(sys.argv[1:]) < 1:
			raise ValueError("Length of argument has to be atleast 1")
		if len(sys.argv[1:]) > 4: 
			raise ValueError("Length of arguments passed cannot be more than 2")
	except ValueError as err:
		print err
		sys.exit()
	except Getopt.getopt as e:
		print e
		sys.exit()
	start = 1
	end=-1

	for o,a in opt:
		if o in ("-s","--start"):
			start = int(a)
		if o in ("-e","--end"):
			end = int(a)
	if end == -1:
		end = start + 100
	print "Range of the numbers are ",start," ",end
	hashlist = [0]*(end - start + 1)
	myqueue = Queue.Queue()
	gg = int (math.sqrt(end)+1)
	print gg
	for i in range(2,gg):
		myqueue.put(i)
	for i in range(0,3):
		t = PrimeSieve(myqueue,i)
		t.setDaemon(False)
		t.start()
	myqueue.join()
	print "Threads have finished"
	for i in range(len(hashlist)):
		if hashlist[i]==1:
			print i+start,
	
if __name__ == '__main__':
	main()