#!/bin/env/python3
""" ProgramDetail.py """
import inquirer
class Selections:
	_questions = [ 
	    inquirer.Checkbox( "aitp programming", 
	    	            message="what aitp programs are you interested in?", 
	    	            choices= [
	    	                "JOIN AITP", 
	    	                "MISION:DATA", 
	    	                "DESIGN_PREVIEW-SHIP", 
	    	                "ECHO LOCAL", 
	    	            ],
	    	            default=None
	    	         )
	    ]
	def __init__(self):
		self.selections = None
	def get(self):
		return self.selections
	def set(self, selections):
		self.selections = selections
	def make(self):
		try:
			selections = inquirer.prompt( self._questions )
			self.set( selections )
			self.view()
		except Exception:
			print( "an exception has occured." )
			print( "possible that the inquirer is broken or unlinked." )
	def view(self):
		if self.selections == None:
			print( "no selections have been made yet." )
			return
		print("your selections:")
		for item in self.selections['aitp programming']:
			print(f"> { item }")
