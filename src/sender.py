# The FileSender class
#
# This client will make delivery attempts for outgoing traffic, and keep
# an in-memory database on timing for each delivery attempt.  Attempts
# are made with exponential backoff.
#
# When started, there is an attempt to deliver as soon as possible.  Upon
# success, the delivered file is deleted.  Upon failure, the delivered
# file is kept from its last change timestamp to the current time.  The
# file is erased when the scheduled date has passed.
#
# When this process receives a USR1 signal, it will re-read the outgoing
# queue for latest modification time stamps, and possible conclude to
# deliver faster if it has been touched since the last delivery attempt.
#
# This process will make all outgoing connections from a predefined
# IP address and port, which may be setup in SRV records for checking.
#TODO# Consider other DNS definitions for the client address/port?
#
# From: Rick van Rein <rick@openfortress.nl>


from threading import Thread, Event
from socket import *
from os import listdir, unlink, stat, access, R_OK, W_OK
from os import sep as slash
from time import time, sleep


class FileSender (Thread):

	def __init__ (self, coords, spool, hosted):
		Thread.__init__ (self)
		self.setDaemon (False)
		self.coords = coords
		self.spool = spool
		self.hosted = hosted
		self.looping = True
		self.queue = { }
		self.timer = Event ()
		self.readqueue ()
		#DEBUG# print 'Queue:', self.queue

	def finish (self):
		self.looping = False
		self.wakeup ()

	def run (self):
		def nop ():
			pass
		#DEBUG# print self.coords
		while self.looping:
			if self.timer.isSet ():
				self.timer.clear ()
				self.readqueue ()
			pause = self.runqueue () - time ()
			pause = max (1, min (pause, 3600))
			print 'Sleeping for', pause, 'seconds'
			self.timer.wait (pause)

	def wakeup (self):
		"""During most of its active life, the FileSender thread is
		   sleeping.  If changes are made to the local filesystem
		   however, it may need to be notified through a call to
		   this function.  Its response will be to reload the queue
		   and recalculate processing times, so this would be a
		   suitable response after any change, even after a mere
		   touch of a file that needs immediate attention.
		"""
		self.timer.set ()
		try:
			self.timer.cancel ()
		except:
			pass

	def nextacttime (self, path):
		now = time ()
		try:
			chg = stat (path).st_mtime
			nxt = now + max (1, now - chg)
			return nxt
		except:
			# There is a problem.  Perhaps the file has gone.
			# Examine quickly what the problem is.  Just don't
			# run wild, so wait 1 second before doing so.
			return now + 1

	def readqueue (self):
		for indom in listdir (self.spool):
			for inusr in listdir (self.spool + slash + indom):
				for inuid in listdir (self.spool + slash + indom + slash + inusr):
					qit = self.spool + slash + indom + slash + inusr + slash + inuid
					try:
						nxt = self.nextacttime (qit)
						if nxt < self.queue [qit]:
							self.queue [qit] = nxt
					except:
						# Exception causes include
						# parallel processes removing
						# this file while working it
						self.queue [qit] = 0

	def runqueue (self):
		now = time ()
		timer = now + 3600
		#DEBUG# print 'RUN QUEUE WITH', len (self.queue.keys ()), 'KEYS'
		for path in self.queue.keys ():
			#DEBUG# print 'Looking into', path
			try:
				if self.queue [path] <= now:
					del self.queue [path]
					self.submit (path)
				if self.queue.has_key (path) and self.queue [path] < timer:
					timer = self.queue [path]
					#DEBUG# print 'Lowered timer to', timer - time ()
			except:
				# Something wrong, perhaps changes to the
				# queue.  Ignore and continue.
				pass
		#DEBUG# print 'RAN QUEUE AND DONE FOR', timer - time (), 'SECONDS'
		return timer

	def submit (self, path):
		try:
			#DEBUG# print 'Would now like to submit ' + path #+ ':\n' + str (cal)
			rdom = path.split (slash) [-3]
			hostports = self.lookup_hostports (rdom)
			been_connected = False
			for (host,port) in hostports:
				print 'Looking for connection to', host + ':' + str (port)
				ips = [gethostbyname (host)]
				for ip in ips:
					print 'Trying connection to', ip + ':' + str (port)
					try:
						sox = socket (AF_INET, SOCK_STREAM, 0)
						print 'Binding to ' + self.coords [0] + ':' + str (self.coords [1])
						sox.bind (self.coords)
						print 'Connecting to ' + ip + ':' + str (port)
						sox.connect ( (ip,port) )
						been_connected = True
						print 'Been connected!'
						#TODO# TLS Pool setup
						try:
							if self.send_file (sox, path):
								self.sent_file (path)
								#TODO:TEST=KEEP# unlink (path)
						except:
							pass
						#TODO# TLS Pool teardown
						sox.close ()
					except:
						pass
					if been_connected:
						break
				if been_connected:
					break
			raise Exception ('#TODO:TEST=KEEP#')
		except:
			# Something went wrong.  Respond to any unorderly
			# behaviour by requeueing the item.  Do this with
			# exponential fallback.  Note that passing the
			# time of an event causes it to be dropped in an
			# orderly manner, so without ending up in this branch
			# of execution.
			if access (path, R_OK|W_OK):
				self.queue [path] = self.nextacttime (path)
				#DEBUG# print 'Deferring for', self.queue [path] - time (), 'seconds'


	#
	# Subclass API starts here
	#

	def lookup_hostports (self, rdomain):
		"""Return the list of (hostname,port) pairs that may be
		   connected to, in order of preference.

		   This function may be overridden by the subclass.  It has
		   a useful default behaviour only if SRV labels were setup
		   during initialisation, using srvlabel="_xxx._yyy".

		   The hostnames in the list are tried in order, until one
		   succeeds at connecting.  For each, an IPv6 lookup and an
		   IPv4 lookup will be made, inasfar as these are setup when
		   this object wa initialised.

		   An empty list will be interpreted as an error at delivery,
		   and later retries will be prepared.
		"""
		return [ ('localhost',55667) ] #TODO:TEST#
		if not self.srvlabel:
			raise NotImplementedError ('Please provide srvlabel="_xxx._yyy" during initialisation or subclass FileSender.lookup_hosts')


	def send_file (self, sox, path):
		"""The send_file procedure is a request to send the file using
		   whatever protocol is deemed suitable.  The connection has
		   been established, and mutual authentication and
		   authorization has taken place.

		   Use sox as the outgoing socket, and path as the filename
		   leading to the file to be sent.

		   This function must be overridden in subclasses of
		   FileSender, or otherwise a runtime exception will be
		   raised.

		   Return True on success, or False on error.  Uncaught
		   exceptions count as a False return value.  If the file
		   continues to exist on error, then another attempt will
		   be made at sending the file.
		"""
		#TODO:TEST# raise NotImplementedError ('FileSender.send_file should be overridden in a subclass')
		print 'FileSender.send_file should be overridden in a subclass'
		sox.send (open (path).read ())

	def sent_file (self, path):
		"""A notification that the file has been sent, and is ready
		   to be removed from the FileSender file structures.

		   The path is the filename of the file that was sent.

		   If the subclass is interested in such notifications, it
		   may override this function.  It may even remove the file
		   if it thinks it is in a better position to do this.
		"""
		pass


