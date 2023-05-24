#!/bin/env/python3
""" 
    @module ProgramContext.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes a model for program context.
"""
class ProgramContext:
	_programs = [ 
	    
	    { 
	        "program":  "join aitp",  
	        "description": [
	             "become a member.",
	             "we do coffee && tea"
	        ],
	    },

	    {
	        "program": "mission:data",
	        "description": [
	            "learn about data you created on social media platforms.",
	            "goal: meet meta you"
	        ],
	        
	    },

	    {
	        "program": "echo local",
	        "description": [
	            "short session on using your computer's terminal ( or shell )",
	            "a power-up to your computing experience"
	        ],
	    },

	    {
	        "program": "design_preview_ship",
	        "description": [
	            "platform to launch emerging entities within the information technology space.",
	            "aitp's emerging ventures lab.",
	            "we fund, design, and develop real-world new-business prototypes."
	            ],
	    },

	    {
	        "program": "azure immersion",
	        "description": [
	            "gain enterprise skills via learning microsoft azure.",
	            "hosted by advisor nguyen"
	            ],
	    },


	]
	def __init__(self):
		""" constructor """
		self.programs = self._programs
	def view(self):
		"""
		    @method get
		    @purpose prints contents of programs to console.
		    @return void
		"""
		print("\n---- aitp programs ---- ")
		for element in self.programs:
			print("")
			print( element['program'].upper() )
			for desc in element['description']:
				print(f"> { desc }" )
		print("\n")