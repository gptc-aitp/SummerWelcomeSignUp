`last modified: 2023 MAY 20`

# SignUpForm
This python application is to be used during GPTC's Summer Welcome week. The purpose of the application is to intake student interest and contact information. As of writing, this application runs on a local machine from the command-line.

## Installation
* Clone the repository
	- `cd ~ && gh repo clone gptc-aitp/SummerWelcomeSignUp`
* change into the directory
	- `cd SummerWelcomeSignUp`
* Install packages
	- `pip3 install -r requirements.txt`
* Run the application
	- `python3 src/app.py`

## Design
The design of the application follows this pattern:
* Welcome
* Input
	- First name
	- Last name
	- Email
	- Selected Interests
* Save Input to .txt file
	- `/SignUpForm/dataout/responses.txt`

## Future Work
* Build a GUI.
* Connect to database.
