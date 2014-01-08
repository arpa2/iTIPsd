#!/usr/bin/python
#
# itipsd -- iTIPs daemon, running iTIP as a service over TLS.
#
# From: Rick van Rein <rick@openfortress.nl>


#
# File structure:
#   /var/spool/itipsd/in/<ldomain>/<luser>/<rdomain>/<ruser>/<uid>/text/calendar
#   /var/spool/itipsd/out/<ldomain>/<luser>/<uid>/text/calendar
#   /var/spool/itipsd/free/<ldomain>/<luser>.free
#
# Locking convention:
#   Use flock() to be the sole user working on a file.
#   Bail out from deadlock when acquiring more than one lock at the same time.
#
# Configuration:
#   hosted is a map of locally accepted domains to usernames in it
#   recversockcoords is the incoming (ip,port) on which the daemon is a recver
#   sendersockcoords is the outgoing (ip,port) on which the daemon is a sender
#
# Limitations:
#   - No checking of SRV records for the remote party yet
#   - No TLS Pool is integrated yet (and so no sender checking)
#


hosted = {
	'example.com': [ 'rick', 'michiel' ],
	'example.net': [ 'rick', 'lutz' ],
}

sendersockcoords = ( '127.0.0.1', 55666 )
recversockcoords = ( '127.0.0.1', 55667 )


from sender import FileSender
from recver import FileRecver
from signal import signal, pause, SIGINT, SIGUSR1, SIGUSR2
from sys import exit


recver = FileRecver (recversockcoords, '/var/spool/itipsd/in',  hosted, 'text/calendar')
sender = FileSender (sendersockcoords, '/var/spool/itipsd/out', hosted, 'text/calendar')

def recverwakeup (signum, frame):
	#DEBUG# print 'Waking up recipient for a reload'
	recver.wakeup ()

def senderwakeup (signum, frame):
	#DEBUG# print 'Waking up sender for a reload'
	sender.wakeup ()

def interrupt (signum, frame):
	print 'Please wait while closing down itipsd with some dignity'
	sender.finish ()
	recver.finish ()
	exit (1)

signal (SIGINT, interrupt)
signal (SIGUSR1, senderwakeup)
signal (SIGUSR2, recverwakeup)

recver.start ()
sender.start ()

while True:
	#DEBUG# print 'Waiting for signal'
	pause ()
	#DEBUG# print 'Got signal'

