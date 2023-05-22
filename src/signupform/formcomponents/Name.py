#!/bin/env/python3
""" 
    @module Name.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes a model for a Name.
"""
class Name:
	_namesAdded = 0
	def __init__(self):
		self.firstName = None
		self.lastName = None
		self.fullName = None
	def getFirstName( self ) -> str:
		"""
		    @method getfirstName
		    @purpose getter. returns the instance variable, firstName.
		    @return string
		"""
		return self.firstName
	def setFirstName( self, firstName:str ) -> str:
		"""
		    @method getLastName
		    @purpose setter. returns the instance variable, firstName.
		    @return string
		"""
		self.firstName = firstName
	def getLastName( self ) -> str:
		"""
		    @method getLastName
		    @purpose getter. returns the instance variable, lastName.
		    @return string
		"""
		return self.lastName
	def setLastName( self, lastName ) -> str:
		"""
		    @method setLastName
		    @purpose setter. returns the instance variable, firstName
		    @return string
		"""
		self.lastName = lastName
	def getFullName( self ):
		"""
		    @method getFullName
		    @purpose getter. returns the a concatenation\
		             of the instance variables firstName & lastName.
		    @return string
		"""
		return f"{ self.firstName } { self.lastName }"
	def setFullName( self, firstName, lastName ):
		"""
		    @method setFullName
		    @purpose setter. sets the instance variable, fullName. 
		                     also increases meter by one.
		    @return void
		"""
		self.fullName = f"{ firstName } { lastName }"
		self._namesAdded += 1
	def inputFirstName(self):
		"""
		    @method inputFirstName
		    @purpose triggers input loop. sets firstName.
		    @return void
		"""
		try:
			inputtingName = True
			while inputtingName:
				firstName = str( input( "> first name: " ) )
				if firstName.strip() == "":
					print( "blank entries not allowed" )
				if firstName.strip().upper() != "STOP":
					self.setFirstName( firstName )
					inputtingName = False; break
		except Exception:
			print("an exception has occured.")
	def inputLastName( self ):
		"""
		    @method inputLastName
		    @purpose triggers input loop. sets lastName.
		    @return void
		"""
		try:
			inputtingName = True
			while inputtingName:
				lastName = str( input( "> last ( family ) name: " ) )
				if lastName.strip() == "":
					print( "blank entries not allowed" )
				if lastName.upper() != "STOP":
					self.setLastName( lastName )
					inputtingName = False; break
		except Exception:
			print( "an exception has occured." )
	def view(self):
		"""
		    @method view
		    @purpose prints fullName to console.
		    @return void
		"""
		print( "> your name:", self.getFullName() )