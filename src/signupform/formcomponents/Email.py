#!/bin/env/python3
""" Email.py """
import re
class Email:
	_emailsAdded = 0
	def __init__( self ):
		self.emailAddress = None
	def getEmailAddress( self ):
		return self.emailAddress
	def setEmailAddress( self, emailAddress ):
		self.emailAddress = emailAddress
	def inputEmailAddress( self ):
		validEmail = False
		emailPattern = re.compile( r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@([A-Za-z0-9]+(\.[A-Za-z0-9]+)+)" )
		while validEmail is False:
			emailAddress = str( input( "> enter your gptc email: ") )
			if emailAddress.upper() == "QUIT":
				break
			if self.emailIsValid( emailAddress, emailPattern ) != False:
				self.setEmailAddress( emailAddress )
				self._emailsAdded += 1
				validEmail = True
				break
	def emailIsValid( self, emailAddress, emailPattern ):
		gptcDomain = "student.gptc.edu"
		if re.fullmatch( emailPattern, emailAddress ) and gptcDomain in emailAddress:
			print("valid email")
			return True
		else:
			print( "invalid email" )
			if gptcDomain not in emailAddress:
				print( "email does not contain 'student.gptc.edu'" )
			return False
	def view(self):
		if self.emailAddress != None:
			print( f"email: { self.emailAddress }" )
		else:
			print("an email has not been inputted yet.")
			self.inputEmailAddress()