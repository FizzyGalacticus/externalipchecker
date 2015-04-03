#!/usr/bin/python

import urllib
import smtplib
import time

def sendText(message):
	username = 'example@example.com'				#foo@gmail.com
	password = 'yourpasswordhere'					#password
	recipients = ['Your SMS Gateway Address']		#1234567891@txt.att.net
	message = ('\n' + message)
	
	server = smtplib.SMTP('your smtp server here')	#smtp.gmail.com
	server.ehlo()
	
	if server.has_extn('STARTTLS'):
		server.starttls()
		server.ehlo()
	
	try:
		server.login(username, password)
		server.sendmail(username, recipients, message)
		print "Message sent"
	except:
		print "Failed to login to SMTP server"	
	
	server.quit()

def getOldIP():
	try:
		f = open('externalip.txt', 'r')
		oldIP = f.read()
		f.close()
		return oldIP
	except:
		f = open('externalip.txt', 'w')
		f.write('')
		f.close()
		return ''
	
def setNewIP(newIP):
	f = open('externalip.txt', 'w')
	f.write(newIP)
	f.close()

def checkIP(oldIP):
	newIP = oldIP
	url = 'http://myip.xname.org/'
	
	try:
		newIP = urllib.urlopen(url).read()
		newIP = newIP[0:len(newIP)-1]
	except:
		print "Could not retrieve new IP."
	
	if newIP != oldIP:
		sendText("External IP has changed.\nNew IP: %s" % newIP)
		setNewIP(newIP)
		print "New IP is not equal to the old one!"
	
while(True):
	checkIP(getOldIP())
	time.sleep(3)
