## My helper bot backend
**There was a problem in the json configuration like rows[0] cannot use input directly as we havn't indexed it yet, so create empty rows like this `rows = ['','','']`**


**Function name can't contain `-` so I have changed that to `_`** 
### How to set up backend of the given rules of a bot
> python bot.py assignment_1_input_1.json

this will generate the function of the bot with given rules at `backend/handler.py`

To Run your bot interactively, use the function generated by the god-bot like calling bot function in a python file

Example : 
```
def sample_text_function1():
	print("Hello! I'm Elth. I'm your algorithms bot.")
	first_name = raw_input("Before starting please tell me your first name")
	last_name = raw_input("Please tell me your last name")
	gender = raw_input("And your gender?( Male/female )")
	age = raw_input("May I know your age?")
	while ( ( age.isdigit() == False ) ):
		age = raw_input("I couldn't quite get how that response can be your age :/ Please enter your valid age.")
	print("Congratulations! Registration Successful.")
	full_name = first_name + ' ' + last_name
	print( "Hello %s , How are you? For a sample of my work I can show you how to make a transpose of a 3X3 matrix." % (full_name) )
	rows = ['','','']
	rows[0] = raw_input("Enter the first row of the matrix(3 integers space seperated).")
	rows[1] = raw_input("Enter the second row of the matrix(3 integers space seperated).")
	rows[2] = raw_input("Enter the third row of the matrix(3 integers space seperated).")
	matrix = [map(int, i.split()) for i in rows]
	t_matrix = [[matrix[j][i] for j in xrange(3)] for i in xrange(3)]
	print("This is the transpose of the input matrix")
	for i in range(3):
		print( "Row %i : %s" % (i+1, str(t_matrix[i])) )
	
sample_text_function1()  # testing the bot IQ

```
The conversation is saved in the logs folder with file name by `username-bot-<current-time>.json`