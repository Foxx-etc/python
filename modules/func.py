# prompt : is string to display the instruction what to input
# message : to display Error Like message(warning) if requirements not met
def only_alpha(promt="Enter : ",message="Please Enter Only Letters!\n"):
	while True:
		try:
			name = input(promt)
			if not name.isalpha():
				raise ValueError
			return name
			break
				
		except:
			print(f'{message}')		


# prompt : is string to display the instruction what to input
# message : to display Error Like message(warning) if requirements not met
def only_int(prompt="Enter a Number : ",message="Please Enter a Number!\n"):
	while True:
		
		try:
			user = input(prompt)
			if not user.isdigit():
				raise
			break
			
		except:
			print(message)
			
	return int(user)
    
