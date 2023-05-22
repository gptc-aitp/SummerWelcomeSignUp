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
	             "this is how you become a member.",
	             "help boost aitp member quality, engagement.",
	             "we do coffee && tea"
	        ],
	    },

	    {
	        "program": "mission:data",
	        "description": [
	            "hands-on series on the acquisition, reflection, and re-deployment of personal meta data created by users for social media platforms.",
	            "goal: meet meta you"
	        ],
	        
	    },

	    {
	        "program": "echo local",
	        "description": [
	            "a series of short session on using the computer's terminal ( or shell )",
	            "workshop sprint",
	            "introduces the command-line",
	            "a power-up to your computing experience"
	        ],
	    },

	    {
	        "program": "design_preview_ship",
	        "description": [
	            "a platform to launch emerging entities within the information technology space.",
	            "aitp's emerging ventures lab.",
	            "we fund, design, and develop real-world new-business prototypes."
	            ],
	    },

	    {
	        "program": "git bash",
	        "description": [
	            "on-boards those interested in directly contributing to open aitp projects.",
	            "introduces at least the basics of git ( enough to begin being active )",
	            "we fund, design, and develop real-world new-business prototypes."
	            ],
	    },

	    {
	        "program": "azure immersion",
	        "description": [
	            "gain enterprise skills via learning microsoft azure.",
	            "available to aitp members and gptc students.",
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
		print("\naitp programs:")
		for element in self.programs:
			print("")
			print( element['program'] )
			for desc in element['description']:
				print(f"+ { desc }" )
		print("\n")