#!/bin/env/python3
""" Data.py """
import os
class Data:
	def __init__( self ):
		pass
	def save( self, destination, data ):
		try:
			with open( destination, "a+" ) as source:
				source.write( data + "\n" )
			return
		except FileNotFoundError:
			print( destination, "not found." )
	def retrive(self, destination ):
		try:
			with open( destination, "r" ) as source:
				for line in source:
					source.read( line )
			return
		except FileNotFoundError:
			print( destination, "not found." )