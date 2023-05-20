#!/bin/env/python3
""" Name.py """
class Name:
	_namesAdded = 0
	def __init__(self):
		self.firstName = None
		self.lastName = None
		self.fullName = None
	def getFirstName( self ):
		return self.firstName
	def setFirstName( self, firstName:str ) -> str:
		self.firstName = firstName
	def getLastName( self ):
		return self.lastName
	def setLastName( self, lastName ):
		self.lastName = lastName
	def getFullName( self ):
		return f"{ self.firstName } { self.lastName }"
	def setFullName( self, firstName, lastName ):
		self.fullName = f"{ firstName } { lastName }"
		self._namesAdded += 1
	def inputFirstName(self):
		try:
			inputtingName = True
			while inputtingName:
				firstName = str( input( "> first name: " ) )
				if firstName.strip() == "":
					print( "blank entries not allowed" )
				elif firstName.strip().upper() == "STOP":
					break
				else:
					self.setFirstName( firstName )
					inputtingName = False; break
		except Exception:
			print("an exception has occured.")
	def inputLastName( self ):
		try:
			inputtingName = True
			while inputtingName:
				lastName = str( input( "> last ( family ) name: " ) )
				if lastName.strip() == "":
					print("blank entries not allowed")
				elif lastName.strip().upper() == "STOP":
					break
				else:
					self.setLastName( lastName )
					inputtingName = False; break
		except Exception:
			print( "an exception has occured." )
	def view(self):
		print( "> your name:", self.getFullName() )