#!/usr/bin/python

import sys
import time
import pymongo
import smtplib
from daemon import Daemon
from email.mime.text import MIMEText
from pymongo import MongoClient

class MyDaemon(Daemon):
	logfile = 'tmp/mongo-probe.log'

	def run(self):
		while True:
			time.sleep(60)
			self.prober()

	def prober(self):
		try:
			file(self.logfile,'w+').write("%s\n" % 'Probing\n')	
			client = MongoClient()
		except pymongo.errors.ConnectionFailure:
			self.sendwarning()

	def sendwarning(self):
		file(self.logfile,'w+').write("%s\n" % 'Achtung! Mongo ist gebrochen, kaput!\n')	
		
		'''
    	print 'Sending a warning email'
	    
    	mywarning = 'Achtung! Mongo ist gebrochen, kaput!'
    	msg = MIMEText(mywarning)

    	me = 'mongoprobe1@benchamrkeducation.com'
    	you = 'yves.hoebeke@gmail.com'
    	subject = 'Mongo connectivity issue'

    	msg['Subject'] = subject
    	msg['From'] = me
    	msg['To'] = you

    	s = smtplib.SMTP('localhost')
    	s.sendmail(me, [you], msg.as_string())
    	s.quit()
    	'''

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/daemon-example.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
	else:
		print "usage: %s start|stop|restart" % sys.argv[0]
		sys.exit(2)
