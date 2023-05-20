#!/bin/env/python3
""" Title.py """
class Title:
	
	def __init__( self ):
		self.organization = "(a)ssociation of\n(i)nformation\n(t)echnology\n(p)rofessionals"
		self.applicationPurpose = "student interest and club awareness form"
		self.instructions = [ "follow the prompts", "ask your aitp rep for help" ]
	def create(self):
		print( self.organization, "\n" )
		print( self.applicationPurpose, "\n" )
		print( "instructions" )
		for instruction in self.instructions:
			print(f"> { instruction }")
		print( "----------------------------------------------------------------\n" )
	def view(self):
		print(self.create())