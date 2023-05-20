#!/bin/env/python3
""" ProgramContent.py """
class ProgramContext:
	_programs = [ 
	    
	    { 
	        "program":  "join aitp",  
	        "description": "this is how you become a member.",
	        "callToAction": "we do coffee && tea" 
	    },

	    {
	        "program": "mission:data",
	        "description": "a hands-on series mostly about individual meta-data.",
	        "callToAction": "reclaim your data and meet meta-you?"
	    },

	    {
	        "program": "echo local",
	        "description": "a series of short session on using the computer's terminal ( or shell )",
	        "callToAction": "leave with a power-up to apply!" 
	    },

	    {
	        "program": "design_preview-ship",
	        "description": "a platform to launch emerging entities within the information technology space.",
	        "callToAction": "got entreprenurial spirit?"
	    },
	]
	def __init__(self):
		self.programs = self._programs
	def view(self):
		print("\nprograms:")
		for element in self.programs:
			print( f"> { element['description'] } ( { element['program'].upper() } )" )