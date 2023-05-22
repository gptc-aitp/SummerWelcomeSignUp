#!/bin/env/python3
""" 
    @module ProgramDetail.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes a model for Selections.
"""
import inquirer
class Selections:
	_questions = [ 
	    inquirer.Checkbox( "aitp programming", 
	    	            message="what aitp programs are you interested in?", 
	    	            choices= [
	    	                "join aitp", 
	    	                "mision:data", 
	    	                "design_preview_ship", 
	    	                "echo local", 
	    	                "git bash",
	    	                "azure immersion"
	    	            ],
	    	            default=None
	    	         )
	    ]
    
	def __init__(self):
		""" constructor """
		self.selections = None
	def get(self):
		"""
		    @method get
		    @purpose getter. returns the instance variable, selections.
		    @return list
		"""
		return self.selections
	def set(self, selections):
		"""
		    @method set
		    @purpose setter. sets the instance variable, selections.
		    @return void
		"""
		self.selections = selections
	def make(self):
		"""
		    @method make
		    @purpose triggers selection loop. do the selecting.
		    @return void
		"""
		try:
			selections = inquirer.prompt( self._questions )
			self.set( selections )
			self.view()
		except Exception:
			print( "an exception has occured." )
			print( "possible that the inquirer is broken or unlinked." )
	def view(self):
		"""
		    @method view
		    @purpose prints current selections to console.
		    @return void
		"""
		if self.selections == None:
			print( "no selections have been made yet." )
		print("your selections:")
		for item in self.selections['aitp programming']:
			print(f"> { item }")
