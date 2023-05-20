#!/bin/env/python3
""" Title.py """

class Title:
	default = "aitp student interest form"
	def __init__(self):
		pass
	def create(self):
		print( "(a)ssociation of\n(i)nformation\n(t)echnology\n(p)rofessionals\n" )
		print( "student interest form" )
		print( "instructions: fill out our form to further participate in aitp" )
		print( "----------------------------------------------------------------\n" )
	def view(self):
		print(self.create())