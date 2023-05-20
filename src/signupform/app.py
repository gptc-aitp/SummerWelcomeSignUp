#!/bin/env/python3
""" app.py """
import os
import time
import datacomponents.Data as Data
import datacomponents.Response as Response
import formcomponents.Email as Email
import formcomponents.Name as Name
import formcomponents.Title as Title
import formcomponents.Selections as Selections
if __name__ == "__main__":
	entries = 0
	running = True
	title = Title.Title()
	name = Name.Name()
	email = Email.Email()
	selections = Selections.Selections()
	response = Response.Response()
	data = Data.Data()
	while running:
		title.view()
		print( "entries:", entries )
		name.inputFirstName()
		name.inputLastName()
		email.inputEmailAddress()
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