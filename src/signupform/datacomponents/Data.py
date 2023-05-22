#!/bin/env/python3
""" 
    @module Response.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes model for Data.
"""
import os
class Data:
	def __init__( self ):
		pass
	def save( self, destination:str, data:str ):
		""" 
            @method save
            @param destination:string ( expects a file path )
            @param data:string
            @purpose save formatted data to output.
            @return string
        """
		try:
			with open( destination, "a+" ) as source:
				source.write( data + "\n" )
		except FileNotFoundError:
			print( destination, "not found." )
	def retrive(self, destination ):
		""" 
            @method retrieve
            @param destination:string ( expects a file path )
            @purpose reads output file.
            @return void
        """
		try:
			with open( destination, "r" ) as source:
				for line in source:
					source.read( line )
		except FileNotFoundError:
			print( destination, "not found." )