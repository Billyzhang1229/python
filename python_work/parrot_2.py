prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)
	if messsage == 'quit':
		active = False
	else:
		print(message)