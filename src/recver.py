# The FileRecver class


from threading import Thread
from socket import *
from time import time
from os import write, access, W_OK, makedirs, pipe
from select import select

from os import sep as slash


class FileRecver (Thread):

	def __init__ (self, coords, spool, hosted, mimetp):
		Thread.__init__ (self)
		self.setDaemon (False)
		self.coords = coords
		self.spool = spool
		self.hosted = hosted
		self.mimetp = mimetp
		self.looping = True
		self.srvsox = socket (AF_INET, SOCK_STREAM, 0)
		self.srvsox.setblocking (0)
		self.srvsox.bind (coords)
		self.srvsox.listen (5)
		(self.stoprd, self.stopwr) = pipe ()
		#DEBUG# print 'Listening on', coords

	def finish (self):
		self.looping = False
		self.wakeup ()

	def run (self):
		while self.looping:
			try:
				if self.stoprd in select ([self.srvsox, self.stoprd], [], []) [0]:
					break
				(sox, remote) = self.srvsox.accept ()
				#TODO# Apply TLS Pool and harvest contact identities
				#TODO# Check remote as having a listed SRV record
				localid = 'rick@example.com' #TODO#FIXED#
				remotid = 'lutz@example.net' #TODO#FIXED#
				path = self.spool + slash + 'example.com' + slash + 'rick' + slash + self.mimetp + slash #TODO#FIXED#
				if not access (path, W_OK):
					makedirs (path)
				self.recv_file (sox, path, localid, remotid)
				sox.close ()
			except Exception, e:
				# Some exception in handling -- ignore & cycle
				pass
		self.srvsox.close ()

	def wakeup (self):
		write (self.stopwr, 'HINT')

	#
	# API to subclasses
	#

	def recv_file (self, sox, path, localid, remotid):
		"""Read, process and respond to iTIP messages.  The provided
		   information details the local and remote identities.

		   The sox is a connected TCP socket setup through TLS.
		   The path points to an existing directory where the files
		   for this user can be stored, but only if a spooldir was
		   setup when this object was initialised.  The localid and
		   remotid represent verified local and remote identities,
		   respectively.   They are either in user@domain format or
		   they are just a domain (any combination is possible) and
		   it is up to the receiver function to see if these are of
		   the welcomed forms, and whether they match the contents
		   of the data exchanged.
		
		   This function must be overridden by a subclass.
		"""
		#TODO:TEST# raise NotImplementedError ('FileRecver.recv_file should be overridden in a subclass')
		print 'FileRecver.recv_file should be overridden in a subclass'
		dta = sox.recv (65536)
		tgt = path + str (time ())
		fil = open (tgt, 'w')
		fil.write (dta)
		fil.close ()
		print 'Written data to ' + tgt

