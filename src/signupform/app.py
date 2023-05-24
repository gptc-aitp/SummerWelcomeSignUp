#!/bin/env/python3
""" 
    @module app.py
    @author jack l.
    @date 2023 05 22
    @purpose module describes application's event loop.
"""
import os
import time
import datacomponents.Data as Data
import datacomponents.Response as Response
import displaycomponents.Title as Title
import displaycomponents.ProgramContext as ProgramContext
import formcomponents.Email as Email
import formcomponents.Name as Name
import formcomponents.Selections as Selections
if __name__ == "__main__":
	entries = 0
	running = True
	title = Title.Title()
	context = ProgramContext.ProgramContext()
	name = Name.Name()
	email = Email.Email()
	selections = Selections.Selections()
	response = Response.Response()
	data = Data.Data()
	while running:
		os.system("clear")
		title.view()
		context.view()
		# print( "entries:", entries )
		name.inputFirstName()
		name.inputLastName()
		email.inputEmailAddress()
		time.sleep(1)
		os.system("clear")
		# context.view()
		selections.make()
		response.format( name.getFirstName(), 
			             name.getLastName(),
			             email.getEmailAddress(),
			             selections.get() )
		data.save( "../../dataout/responses.txt", response.get() )
		time.sleep(2)
		entries += 1
		if entries >= 100:
			break
		os.system("clear")